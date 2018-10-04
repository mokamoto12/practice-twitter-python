from src.application.tweet.command import Command
from src.application.tweet.command import Tweet as TweetCommand
from src.domain.model.tweet import TweetRepository, TweetId, Tweet, UserId


class CommandBus:
    def __init__(self, tweet_repository: TweetRepository):
        self.tweet_repository = tweet_repository

    def handle(self, command: Command) -> TweetId:
        if isinstance(command, TweetCommand):
            tweet_id: TweetId = self.tweet_repository.next_identity()
            tweet = Tweet.create(tweet_id, UserId(command.user_id), command.text)
            self.tweet_repository.save(tweet)

            return tweet_id
