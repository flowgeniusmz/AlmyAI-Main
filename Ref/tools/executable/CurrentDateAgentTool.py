#CurrentDateAgentTool

import json
from datetime import date

class CurrentDateAgentTool:
    def get_description(self):
        return 'Returns the current date and time'

    def get_parameters(self):
        return {}

    def execute(self, args):
        return json.dumps(str(date.today()))