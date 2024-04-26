#RUNSOQLAGENT TOOL
from simple_salesforce import Salesforce
import json

class RunSOQLAgentTool:
    def __init__(self, username, password, security_token):
        self.sf = Salesforce(username=username, password=password, security_token=security_token)

    def get_description(self):
        return 'Executes a SOQL query and returns JSON results'

    def get_parameters(self):
        return {
            'sql': 'SQL to execute. May not contain any :variables'
        }

    def execute(self, args):
        # Check if sql argument is present
        if 'sql' not in args:
            raise Exception('Missing required parameter: sql')

        # Get the SOQL query from parameters
        soql = args['sql']

        # Perform the SOQL query
        records = self.sf.query_all(soql)

        # Serialize records to JSON format
        jsonResponse = json.dumps(records)

        return jsonResponse
