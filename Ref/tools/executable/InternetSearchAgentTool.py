import json
import requests

###InternetSearchAgentTool
class InternetSearchAgentTool:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_description(self):
        return 'Search the internet'

    def get_parameters(self):
        return {'query': 'The search query to perform'}

    def execute(self, args):
        query = args.get('query')
        if query is None or query == '':
            raise Exception('Query is empty')

        response = requests.get(
            'https://serpapi.com/search.json',
            params={
                'q': query,
                'hl': 'en',
                'gl': 'us',
                'api_key': self.api_key
            }
        )

        if response.status_code == 200:
            data = response.json()

            results = {
                'answer': data.get('answer_box'),
                'organicResults': data.get('organic_results')
            }

            return json.dumps(results)
        else:
            raise Exception('API returned status code ' + str(response.status_code))