import requests


class BaseApiOperations:
    BASE_URL = "https://slack.com/api/{}"
    TOKEN = "xoxp-878902350102-878554220535-880198090196-3d8765abed2543dc50290cf49af15ce7" #replace token
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

