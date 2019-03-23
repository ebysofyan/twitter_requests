"""
Just a simple sample
"""
import sys
import time

from .generator import TwitterBearerGenerator
from .twitter import Twitter, TwitterQueryBuilder

QUERY = sys.argv[1]
EPOCH = 0

KEYS = {
    'api_key': 'YOUR_API_KEY',
    'api_secret_key': 'YOUR_API_SECRET_KEY'
}
TWITTER_BEARER_GEBERATOR = None
TOKEN = None

while True:
    EPOCH = EPOCH + 1
    if not isinstance(TWITTER_BEARER_GEBERATOR, TwitterBearerGenerator):
        TWITTER_BEARER_GEBERATOR = TwitterBearerGenerator(KEYS)
        TOKEN = TWITTER_BEARER_GEBERATOR.generate_token()
        QUERY_BUILDER = TwitterQueryBuilder.builder().set_count(10)\
            .set_lang('id').build()
        TWITTER_SCRAPPER = Twitter(TOKEN, QUERY_BUILDER)

    try:
        TWITTER_SCRAPPER.find_tweets(QUERY)
        for tweet in TWITTER_SCRAPPER.get_tweets_statuses():
            print(f"{tweet['user']['name']} ==> {tweet['text']} ")
        print(f"====================== END LINE OF EPOCH {EPOCH} ======================")
        time.sleep(60)
    except Exception as e:
        TWITTER_BEARER_GEBERATOR = None
        TOKEN = None

        time.sleep(60)
