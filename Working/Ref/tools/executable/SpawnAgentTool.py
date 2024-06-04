#spawnagenttool

class SpawnAgentTool:
    def __init__(self, tool_description, tool_parameters, chat_model, tools):
        self.tool_description = tool_description
        self.tool_parameters = tool_parameters
        self.chat_model = chat_model
        self.tools = tools
        self.parent_agent = None

    def execute(self, args):
        prompt = ReActZeroShotChatPrompt(self.tools)
        objective = 'Your job is to ' + self.tool_description + '.  Here are the parameters of the task: \n' + self.format_input_parameters(args)
        agent = ReActChatAgent(objective, prompt, self.chat_model)
        self.parent_agent.spawned_agent = agent
        return ReActChatAgent.NO_RESPONSE

    def get_description(self):
        return self.tool_description

    def get_parameters(self):
        return self.tool_parameters

    def format_input_parameters(self, input):
        input_descriptions = []
        for arg_key in input.keys():
            arg_description = self.tool_parameters.get(arg_key)
            input_descriptions.append(arg_description + ': ' + input.get(arg_key))
        return '\n'.join(input_descriptions)
