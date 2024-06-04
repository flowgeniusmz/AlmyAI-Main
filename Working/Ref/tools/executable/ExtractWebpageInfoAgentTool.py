##GetWebpage Tool

import requests
import json
from openai import ChatCompletion

class ExtractWebpageInfoAgentTool:
    def __init__(self, api_key, summerization_model):
        self.api_key = api_key
        self.summerization_model = summerization_model

    def get_description(self):
        return 'find information in webpage'

    def get_parameters(self):
        return {
            'url': 'The url/link of the webpage to search in',
            'targetInfo': '(optional) A general description of the information you are looking for'
        }

    def execute(self, args):
        url = args.get('url')
        target_info = args.get('targetInfo')

        if not url:
            raise Exception('Error: Missing required parameter "url".')

        response = requests.get(f'https://extractorapi.com/api/v1/extractor/?apikey={self.api_key}&url={url}&fields=text,raw_text,clean_html')
        result = response.json()

        if response.status_code != 200:
            raise Exception(f'Failed to extract text from the URL. Status code: {response.status_code}, Status: {result["status"]}')

        web_text = result['clean_html'] if len(result['clean_html']) < 4000 else result['raw_text'] if len(result['raw_text']) < 4000 else result['text'] if len(result['text']) < 4000 else result['text'][:4000]

        if target_info:
            
            chat_model = ChatCompletion.create(
                model=self.summerization_model,
                messages=[
                    {"role": "system", "content": "Your job is to find and return the requested information from webpage text. Be concise, yet complete"},
                    {"role": "user", "content": f'Requested Info:\n"""{target_info}"""\n\nWebpage:\n"""{web_text}"""'}
                ]
            )
            return chat_model.choices[0].message['content']
        else:
            return result['text']
