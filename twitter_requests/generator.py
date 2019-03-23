"""
This class contains bearer authentication generator
"""
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class TwitterBearerGenerator(object):
    """
    Generate twitter bearer token to authorize your request.
    Your token should be include in headers every request.
    Parameter :
        >>> keys : This keys is dict. You should pass api_key and api_secret_key
    """

    def __init__(self, keys: dict):
        """
        keys contains api_key and api_secret_key
        """
        try:
            self.auth = HTTPBasicAuth(keys['api_key'], keys['api_secret_key'])
            self.client = BackendApplicationClient(client_id=keys['api_key'])
            self.oauth = OAuth2Session(client=self.client)

            self.token_url = 'https://api.twitter.com/oauth2/token'
        except KeyError:
            raise KeyError("keys parameter should contain api_key and api_secret_key")

    def generate_token(self):
        """
        this function will return the result of created token
        """
        result = self.oauth.fetch_token(token_url=self.token_url, auth=self.auth)
        return result['access_token']
