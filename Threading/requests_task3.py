import threading
import requests
import json
import os


class CommentsDownload(threading.Thread):

    def __init__(self, author, parameters):
        super().__init__()
        self._author = author
        self._parameters = parameters

    def run(self):
        response = requests.get(URL, params=self._parameters)
        if response.ok:
            with open(FILE, 'a+') as file:
                json.dump(response.json(), file, indent=4)
                file.write(',\n')
        else:
            raise Exception('Not OK')


URL = 'https://api.pushshift.io/reddit/comment/search'
FILE = 'comments.json'

author_list = ['SweetReptile',
               'toofarbyfar',
               'ImAnonymous135',
               'crescentcactus',
               'AdelineKraxx',
               'bradg2415'
               ]

for author in author_list:
    params = {'size': 5, 'author': author, 'fields': ('author', 'body', 'created_utc')}
    thread = CommentsDownload(author, params)
    thread.start()
    thread.join()

with open(FILE, 'rb+') as file:
    file.seek(-2, os.SEEK_END)
    file.truncate()
