import json
import plyvel
import uuid
from src.domain.model.tweet import TweetRepository, TweetId, Tweet


class LevelDBTweetRepository(TweetRepository):
    def __init__(self, file: str):
        self.db = plyvel.DB(file, create_if_missing=True)

    def next_identity(self) -> TweetId:
        return TweetId(uuid.uuid4().hex)

    def save(self, tweet: Tweet) -> None:
        self.db.put(tweet.tweet_id.value.encode('utf-8'), json.dumps(tweet.to_dict()).encode('utf-8'))
