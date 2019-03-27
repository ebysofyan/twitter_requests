# Moved into https://github.com/nahlalabs/twitter_requests
# Simple python lib to acquire twitter data
[![PyPI version](https://badge.fury.io/py/twitter-requests.svg)](https://badge.fury.io/py/twitter-requests)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/twitter-requests.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An easy and simple python library that allow you to get twitter data through twitter API.

## Installation
For this installation, make sure you have already install `python-pip` on your machine <br/><br/>
`pip install twitter-requests`

## How to use?
This library require `API_KEY` and `SECRET_API_KEY` that you create from https://developer.twitter.com/
<br/>
### 1. Create bearer token by passing `API_KEY` and `SECRET_API_KEY` 
```
from twitter_requests.generator import TwitterBearerGenerator

KEYS = {
    'api_key': 'YOUR_API_KEY',
    'api_secret_key': 'YOUR_API_SECRET_KEY'
}

TWITTER_BEARER_GEBERATOR = TwitterBearerGenerator(KEYS)
TOKEN = TWITTER_BEARER_GEBERATOR.generate_token()
```

You will get bearer token by call `generate_token` method. The type of `TOKEN` is `str`.
<br/>
<br/>
### 2. Lets get the tweets data 
```
from twitter_requests.twitter import Twitter, TwitterQueryBuilder

QUERY_BUILDER = TwitterQueryBuilder.builder().set_count(10)\
            .set_lang('id').build()

TWITTER = Twitter(TOKEN, QUERY_BUILDER)

TWITTER.find_tweets(QUERY)

for tweet in TWITTER.get_tweets_statuses():
    print(f"{tweet['user']['name']} ==> {tweet['text']} ")
```
<br/>

### 3. Enjoy it and do everything you want with your data.
