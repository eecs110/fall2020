import traceback
import sys
import urllib.request
from urllib.request import urlopen
import json
from apis import utilities

try:
    from apis import my_token
    API_TUTOR_TOKEN = my_token.API_TUTOR_TOKEN
except:
    title = 'IMPORTANT: You Need an Access Token!'
    error_message = '\n\n\n' + '*' * len(title) + '\n' + \
        title + '\n' + '*' * len(title) + \
        '\nNavigate to the CS110 Canvas website and open the Project 2 assignment description to get the token.\nThen replace lines 8-16 with API_TUTOR_TOKEN = "THE_CLASS_TOKEN"\n\n'
    raise Exception(error_message)



def get_token(url):
    try:
        response = urlopen(url + '?auth_manager_token=' + API_TUTOR_TOKEN)
        data = response.read()
        results = data.decode('utf-8', 'ignore')
        return json.loads(results)['token']
    except urllib.error.HTTPError as e:
        # give a good error message:
        error = utilities.get_error_message(e, url)
    raise Exception(error)