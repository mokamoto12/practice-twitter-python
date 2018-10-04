import json
import plyvel
from typing import List, Dict


class ContentData:
    def __init__(self, text: str):
        self.text = text


class TweetData:
    def __init__(self, tweet_id: str, user_id: str, content: ContentData):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.content = content


class Query:
    def __init__(self, file: str):
        self.db = plyvel.DB(file)

    def time_line(self) -> List[dict]:
        return [json.loads(tweet.decode('utf-8')) for tweet_id, tweet in self.db.iterator()]

    def user_time_line(self, user_id: str) -> List[dict]:
        return [json.loads(tweet.decode('utf-8')) for tweet_id, tweet in self.db.iterator() if
                json.loads(tweet.decode('utf-8'))['user_id'] == user_id]
