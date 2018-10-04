from abc import ABC


class Command(ABC):
    pass


class Tweet(Command):
    def __init__(self, user_id: str, text: str):
        self.user_id = user_id
        self.text = text
