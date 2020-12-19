import pytest
from requests_oauthlib import OAuth1
import requests
import json
def test_tweet_content():
        tweetresponseUrl = 'https://api.twitter.com/1.1/statuses/show/1257326183101980673.json'
        auth = OAuth1('W7iObSIMUlUwzkNbmTpuyJdwy', 'UJgNXv6I9sZWmm4Y64vyO61w0GylqgTz8MhFc3m3yL19WQFi8o','787905137742192640-YWLL6LFZhDmZ96xk7jA6OkFfBmVc99v', 'M22P323dlh1PcuBqcMtTheaKhWRLPPTNzstmoK90roVE7')
        response = requests.get(tweetresponseUrl, auth=auth)
        formattedResponse = response.json()
        stripped =  (repr(formattedResponse['text']).strip('"\''))
        print(stripped)
        with open('tweetcontent', 'w') as f:
            f.write(formattedResponse['text'])
        f = open("tweetcontent", "r")
        fileread =  (repr(f.read()).strip('"\''))  
        assert fileread == formattedResponse['text']

