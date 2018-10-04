from abc import ABC
from abc import abstractmethod
from datetime import datetime


class UserId:
    def __init__(self, value):
        self.value = value


class Content:
    def __init__(self, text: str):
        self.text = text

    def to_dict(self) -> dict:
        return {
            'text': self.text
        }


class TweetId:
    def __init__(self, value):
        self.value = value


class CreatedAt:
    def __init__(self, date: datetime):
        self.date = date

    @staticmethod
    def now() -> 'CreatedAt':
        return CreatedAt(datetime.now())

    def to_string(self) -> str:
        return self.date.isoformat()


class Tweet:
    def __init__(self, tweet_id: TweetId, user_id: UserId, content: Content, created_at: CreatedAt):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at

    def to_dict(self) -> dict:
        return {
            'tweet_id': self.tweet_id.value,
            'user_id': self.user_id.value,
            'content': self.content.to_dict(),
            'created_at': self.created_at.to_string()
        }

    @staticmethod
    def create(tweet_id: TweetId, user_id: UserId, content: str) -> 'Tweet':
        return Tweet(tweet_id, user_id, Content(content), CreatedAt.now())


class TweetRepository(ABC):
    @abstractmethod
    def next_identity(self) -> TweetId:
        pass

    @abstractmethod
    def save(self, tweet: Tweet) -> None:
        pass
