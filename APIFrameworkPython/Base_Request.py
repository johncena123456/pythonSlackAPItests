import requests


class BaseApiOperations:
    BASE_URL = "https://slack.com/api/{}"
    TOKEN = "REPLACE_TOKEN_HERE" #replace token
    JSON_HEADERS = {'Content-type': 'application/json'}
    URLENCODED_HEADERS = {'Content-type': 'application/x-www-form-urlencoded'}

    def get_call(self, slack_method, parameters):
        parameters.update({'token': self.TOKEN})
        response = requests.get(self.BASE_URL.format(slack_method), params=parameters).json()
        return response

    def post_call(self, slack_method, parameters):
        print ("post Called")
        parameters.update({'token': self.TOKEN})
        response = requests.post(self.BASE_URL.format(slack_method), headers=self.URLENCODED_HEADERS, params=parameters).json()
        return response

