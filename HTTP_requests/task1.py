import requests


url = 'https://www.wikipedia.org/robots.txt'

response = requests.get(url).content.decode()

with open('robots.txt', 'a+') as f:
    f.write(response)
    f.close()
