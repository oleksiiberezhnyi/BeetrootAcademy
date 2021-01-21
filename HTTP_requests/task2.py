import requests
import json


url = 'https://api.pushshift.io/reddit/comment/search/'

response = json.loads(requests.get(url).content.decode())
with open('comments.json', 'w+') as f:
    for i in response['data']:
        time = i['retrieved_on']
        text = i['body']
        string = {time: text}
        json.dump(string, f, indent=4, sort_keys=True, separators=('', ':'))
    f.close()

