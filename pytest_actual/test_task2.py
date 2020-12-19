import pytest
from requests_oauthlib import OAuth1
import requests
import json


@pytest.fixture
def auth():
		my_consumer_key ="customer_key"
		my_consumer_secret ="secret_no"
		my_access_token ="token_no"
		my_access_token_secret ="secret_token"
		return [my_consumer_key,my_consumer_secret,my_access_token,my_access_token_secret]

def test_createtweet():
		createTweetUrl = 'https://api.twitter.com/1.1/statuses/update.json'
		print ('Hi')
		auth = OAuth1('W7iObSIMUlUwzkNbmTpuyJdwy', 'UJgNXv6I9sZWmm4Y64vyO61w0GylqgTz8MhFc3m3yL19WQFi8o','787905137742192640-YWLL6LFZhDmZ96xk7jA6OkFfBmVc99v', 'M22P323dlh1PcuBqcMtTheaKhWRLPPTNzstmoK90roVE7')
		print(auth)
		myObj = {'status' : 'Hi,'}
		response = requests.post(createTweetUrl, auth=auth, data=myObj)
		formattedResponse = response.json()
		for key, value in formattedResponse.items():print(key, ":", value)
		# get id 
		id = (formattedResponse['id'])
		# stringify id
		converted_id = str(id)
		# tweet response
		tweetresponseUrl = 'https://api.twitter.com/1.1/statuses/show/'+converted_id+'.json'
		response = requests.get(tweetresponseUrl, auth=auth)
		formattedResponse = response.json()
		for key, value in formattedResponse.items():print(key, ":", value)
		# get the retweet count
		retweet_count = formattedResponse['retweet_count']
		assert retweet_count == 0
        # retweet
		retweetresponseUrl = 'https://api.twitter.com/1.1/statuses/retweet/'+converted_id+'.json'
		response = requests.post(retweetresponseUrl, auth=auth)
		formattedResponse = response.json()
		for key, value in formattedResponse.items():print(key, ":", value)
		# get the retweet count
		retweet_count = formattedResponse['retweet_count']
		# assert if its 1
		assert retweet_count == 1 
		# retweeters ID
		tweetresponseUrl = 'https://api.twitter.com/1.1/statuses/retweets/'+converted_id+'.json'
		response = requests.get(tweetresponseUrl, auth=auth)
		formattedResponses = json.loads(response.text)
	    # get the retweet ID
		for formattedResponse in formattedResponses:		
			print(formattedResponses[0])
		# unretweet 
		unretweetresponseUrl = 'https://api.twitter.com/1.1/statuses/unretweet/'+converted_id+'.json'
		response = requests.post(unretweetresponseUrl, auth=auth)
		formattedResponse = response.json()
		for key, value in formattedResponse.items():print(key, ":", value)
		# get the retweet count
		retweet_count = formattedResponse['retweet_count']
		# assert if its 1
		assert retweet_count == 1
		# tweet response
		tweetresponseUrl = 'https://api.twitter.com/1.1/statuses/show/'+converted_id+'.json'
		response = requests.get(tweetresponseUrl, auth=auth)
		formattedResponse = response.json()
		for key, value in formattedResponse.items():print(key, ":", value)
		# get the retweet count
		retweet_count = formattedResponse['retweet_count']
		assert retweet_count == 0
		destroyUrl = 'https://api.twitter.com/1.1/statuses/destroy/'+converted_id+'.json'
		response = requests.post(destroyUrl, auth=auth)       

        

            
