import time
import threading
import requests
import json
import os
from dataclasses import dataclass
from typing import List


URL = 'https://api.pushshift.io/reddit/comment/search'
FILE = 'comments.json'


def custom_default(o):
    if isinstance(o, CommentDict):
        return o.dict()


setattr(json.JSONEncoder, 'default', custom_default)


class CommentDict:

    def __init__(self, author, body, created_utc):
        self.author = author
        self.body = body
        self.created_utc = created_utc

    def dict(self):
        return dict(author = self.author,
                    body = self.body,
                    created_utc = self.created_utc
                    )


class AllComments(threading.Thread):

    def __init__(self, query: dict, file_lock: threading.RLock, limit: int = 10000, user_nickname: str = None):
        super().__init__()
        self.query = query
        self._limit = limit
        self.file_lock = file_lock
        self._comments = []
        self._min_comment_created_utc = int(time.time() * 1000)
        self._continue_requesting = True
        if user_nickname:
            self.query['author'] = user_nickname

    def run(self):
        while len(self._comments) < self._limit and self._continue_requesting:
            self.query['size'] = self._min_comment_created_utc
            response: requests.Response = requests.get(URL, params=self.query)
            if not response.ok:
                time.sleep(2)
                continue
            self._process_response(response)
        else:
            self._save()

    def _process_response(self, response):
        response_data_json = response.json().get('data')
        if not response_data_json:
            self._continue_requesting = False
            return
        for comment in response_data_json:
            self._comments.append(
                CommentDict(author=comment.get('author'),
                            body=comment.get('body'),
                            created_utc=comment.get('created_utc')
                            )
                                )
        self._min_comment_created_utc = self._get_min_comment_created_utc()

    def _get_min_comment_created_utc(self):
        return min(comment.created_utc for comment in self._comments)

    def _get_file_comments(self) -> List[CommentDict]:
        data = []
        if not os.path.exists(FILE):
            return data
        with open(FILE) as f:
            comments = json.loads(f.read())
            for comment in comments:
                data.append(
                    CommentDict(
                        author=comment.get('author'),
                        body=comment.get('body'),
                        created_utc=comment.get('created_utc')
                                )
                            )
        return data

    def _save(self):
        self.file_lock.acquire()
        try:
            file_comments = self._get_file_comments()
            self._comments += file_comments
            self._comments.sort(key=lambda comment: comment.created_utc)
            with open(FILE, 'w') as f:
                f.write(json.dumps(self._comments))
        finally:
            self.file_lock.release()


params = dict(
    size=500,
    fields=['created_utc', 'author', 'body']
)

threads = []
file_lock = threading.RLock()

for name in ['Dictiker', 'bursethmichael', 'boiyeet4774', 'Podgorski37', 'Joltemon']:
    comments_downloader = AllComments(params, file_lock, user_nickname=name)
    comments_downloader.start()
    threads.append(comments_downloader)

for thread in threads:
    thread.join()

data = []

with open(FILE) as f:
    comments = json.loads(f.read())
    for comment in comments:
        data.append(
            CommentDict(author= comment.get('author'),
                        body = comment.get('body'),
                        created_utc = comment.get('created_utc')
                        )
                    )