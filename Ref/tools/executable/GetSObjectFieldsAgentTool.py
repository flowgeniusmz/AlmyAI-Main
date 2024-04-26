###GetSObjectFieldsAgentTool
from simple_salesforce import Salesforce
import json

class GetSObjectFieldsAgentTool:
    def __init__(self, username, password, security_token):
        self.sf = Salesforce(username=username, password=password, security_token=security_token)

    def get_description(self):
        return 'Get fields metadata for a SObject'

    def get_parameters(self):
        return {
            'sobject': 'API Name of the SObject'
        }

    def execute(self, args):
        sobject = args.get('sobject')

        if not sobject:
            raise Exception('Missing parameter: sobject.')

        description = getattr(self.sf, sobject).describe()

        fields = []
        for field in description['fields']:
            field_info = {
                'name': field['name'],
                'type': field['type']
            }
            if field['type'] == 'reference':
                field_info['referenceTo'] = field['referenceTo']
            fields.append(field_info)

        return json.dumps(fields, indent=4)