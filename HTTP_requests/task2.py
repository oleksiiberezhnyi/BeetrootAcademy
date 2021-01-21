import requests
import json


URL = 'https://api.pushshift.io/reddit/comment/search/'

response = json.loads(requests.get(URL).text)
with open('comments.json', 'w+') as f:
    for i in response['data']:
        time = i['retrieved_on']
        text = i['body']
        string = {time: text}
        json.dump(string, f, indent=4, sort_keys=True, separators=('', ':'))
