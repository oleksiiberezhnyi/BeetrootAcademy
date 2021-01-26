import requests
from typing import Optional
import json
URL = 'https://api.pushshift.io/reddit/comment/search/'
UNDEFINED = 'undefined'
FILE_NAME = 'comments2.json'
def get_response(url) -> Optional[requests.Response]:
    try:
        return requests.get(URL)
    except Exception:
        print(f'Can not handle GET request to {URL}')
def handle_response(response: Optional[requests.Response]) -> None:
    def save_to_file(payload: dict, file_name: str) -> None:
        with open('comments.json', 'w+') as f:
            if 'data' not in payload:
                return
            for data in payload['data']:
                time = data.get('retrieved_on', UNDEFINED)
                text = data.get('body', UNDEFINED)
                string = {time: text}
                json.dump(string, f, indent=4, sort_keys=True, separators=('', ':'))
    if not response:
        print('Empty response')
    elif not response.ok:
        print('Status is not 200')
    try:
        payload = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print(f'Can not parse to JSON: {response.text}')
        return
    save_to_file(payload, FILE_NAME)
response = get_response(URL)
handle_response(response)