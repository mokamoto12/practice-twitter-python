from flask import Flask
from flask import request
from flask.json import jsonify

from src.application.tweet.command import Tweet
from src.application.tweet.query import Query
from src.application.tweet.service import CommandBus
from src.domain.model.tweet import TweetId
from src.infrastructure.persistence.leveldb.tweet import LevelDBTweetRepository

app = Flask(__name__)

DB_FILE = './storage/database/leveldb/tweet/'


@app.route('/tweet', methods=['POST'])
def tweet():
    tweet_id: TweetId = CommandBus(LevelDBTweetRepository(DB_FILE)).handle(
        Tweet(request.json['user'], request.json['message']))
    return jsonify(tweet_id=tweet_id.value, succusess=True)


@app.route('/tweet', methods=['GET'])
def time_line():
    return jsonify(Query(DB_FILE).time_line())


@app.route('/tweet/<user_id>', methods=['GET'])
def user_time_line(user_id):
    return jsonify(Query(DB_FILE).user_time_line(user_id))
