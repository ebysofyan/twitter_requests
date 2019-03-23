"""
twitter get tweets by anything you want
@created_by ebysofyan 03/22/2019
"""
import requests


class TwitterQueryBuilder(object):
    """
    Create a query param to use in request
    """

    def __init__(self):
        self.paylod = dict(
            count=100,
            result_type="recent",
            lang="en",
            since_id=-1
        )

    @classmethod
    def builder(cls):
        """
        return instance of this class
        """
        return cls()

    def set_count(self, value=100):
        """
        override count query param
        """
        self.paylod['count'] = value
        return self

    def set_result_type(self, value='recent'):
        """
        override result_type query param
        """
        self.paylod['result_type'] = value
        return self

    def set_lang(self, value='en'):
        """
        override lang query param
        """
        self.paylod['lang'] = value
        return self

    def set_since_id(self, value=-1):
        """
        override since_id query param
        """
        self.paylod['since_id'] = value
        return self

    def build(self):
        """
        return a new instance of this class contains new payload
        """
        return self

    def get_payload(self):
        """
        get original payload
        """
        return self.paylod


class Twitter(object):
    """
    Main class for scrap data from twitter periodically
    """

    def __init__(self, bearer_token, query_builder_param: TwitterQueryBuilder):
        self.bearer_token = bearer_token
        self.payload = query_builder_param.get_payload()
        self.time_periodic = ''
        self.tweets = {}

    def find_tweets(self, query):
        """
        find all tweets depend on query
        """

        self.payload['q'] = query
        headers = dict(accept="application/json", Authorization="Bearer " + self.bearer_token)
        base_url = "https://api.twitter.com/1.1/search/tweets.json?"
        url = base_url + "q={q}&count={count}&result_type={result_type}\
                        &lang={lang}&since_id={since_id}".format(**self.payload)
        res = requests.get(url, headers=headers)
        self.tweets = res.json()

    def get_original_tweets_data(self):
        """
        get original data inclue search_metadata and statuses
        """
        return self.tweets

    def get_tweets_statuses(self):
        """
        get all of tweets statuses
        """
        return self.tweets['statuses']

    def get_tweets_search_metadata(self):
        """
        get all of tweets statuses
        """
        return self.tweets['search_metadata']
