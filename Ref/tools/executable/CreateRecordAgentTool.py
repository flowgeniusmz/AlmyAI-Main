###CreateRecordAgentTool
from simple_salesforce import Salesforce
import json
import datetime

class CreateRecordAgentTool:
    def __init__(self, username, password, security_token):
        self.sf = Salesforce(username=username, password=password, security_token=security_token)

    def get_description(self):
        return 'Inserts/Updates records into the database'

    def get_parameters(self):
        return {
            'operation': 'insert|update|upsert',
            'sObjectType': 'The SObject API name',
            'records': 'String of escaped JSON array with record data (fields and values)'
        }

    def execute(self, args):
        sObjectType = args.get('sObjectType')
        fieldsJson = args.get('records')

        if not sObjectType or not fieldsJson:
            raise Exception('Missing parameter(s). Please provide both sObjectType and fields.')

        records = json.loads(fieldsJson)
        operation = args.get('operation')

        ids = []
        for record in records:
            for field, value in record.items():
                if isinstance(value, str) and ('-' in value and ':' in value):
                    try:
                        record[field] = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        record[field] = datetime.datetime.strptime(value, '%Y-%m-%d').date()

            sObject = getattr(self.sf, sObjectType)

            if operation == 'update':
                res = sObject.update(record['Id'], record)
            elif operation == 'upsert':
                res = sObject.upsert(record['Id'], record)
            else: # insert
                res = sObject.create(record)

            ids.append(res['id'])

        return 'New Record Ids: ' + ', '.join(ids)