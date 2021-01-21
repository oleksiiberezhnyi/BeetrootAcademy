import requests


URL = 'https://www.wikipedia.org/robots.txt'

response = requests.get(URL)

if response.status_code == '200':
    with open('robots.txt', 'a+') as f:
        f.write(response.text)
else:
    print(f'Error: {response.status_code}')
