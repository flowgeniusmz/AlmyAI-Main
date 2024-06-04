#SOSLSEARCHAGENTTOOLS

from simple_salesforce import Salesforce
import json

class SOSLSearchAgentTool:
    def __init__(self, username, password, security_token):
        self.sf = Salesforce(username=username, password=password, security_token=security_token)

    def get_description(self):
        return 'Search of salesforce data'

    def get_parameters(self):
        return {
            'term': 'The search term',
            'objectType': 'The SObject to search for'
        }

    def execute(self, args):
        term = args.get('term')
        object_type = args.get('objectType')

        if term is None:
            raise Exception('Missing required parameter: term')

        if object_type is None:
            raise Exception('Missing required parameter: objectType')

        query = f'FIND {{term}} IN ALL FIELDS RETURNING {object_type} LIMIT 10'
        results = self.sf.search(query)

        return json.dumps(results)