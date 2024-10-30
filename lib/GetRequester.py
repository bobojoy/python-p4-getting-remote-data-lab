import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        pass
        print(json.loads(self.get_response_body()))
        return json.loads(self.get_response_body())

data = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
data.load_json()