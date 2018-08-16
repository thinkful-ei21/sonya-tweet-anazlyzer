from textblob import TextBlob
import base64
import requests
import consumer_key from "./keys.py"
import consumer_secret from "./keys.py"
# consumer_key = "YiyW8ZmfLzL1QFGkJM1bZuUUv"
# consumer_secret = "lsQOg4kaQdYkqoscK7LPqaCpiHWWVY4b0RcQnESgMoPAoZlm8j"
key_secret = "{}:{}".format(consumer_key, consumer_secret).encode("ascii")
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode("ascii")

base_url = "https://api.twitter.com/"
auth_url = "{}oauth2/token".format(base_url)

auth_headers = {
  "Authorization": "Basic {}".format(b64_encoded_key),
  "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
}

auth_data = {
  "grant_type": "client_credentials"
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

access_token = auth_resp.json()["access_token"]

search_headers = {
  "Authorization": "Bearer {}".format(access_token)
}

search_params = {
  "q": "trump middle east",
  "result_type": "recent",
  "lang": "en",
  "count": 3
}

search_url = "{}1.1/search/tweets.json".format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()
import pprint
pprint.pprint(tweet_data)

tweets = {}

# pull out text and id from tweet data
for x in tweet_data["statuses"]:
    tweets[x["id"]] = x["text"]

unique_tweets = {}

# remove all duplicate tweets
for key, value in tweets.items():
    if value not in unique_tweets.values():
        unique_tweets[key] = value

# print(unique_tweets)
# print(len(unique_tweets), len(tweets))

tweet_texts = ""

# create a list of tweet text
for key in unique_tweets.values():
    tweet_texts += key

# print(tweet_texts)


# text = TextBlob(" ".join(tweet_texts))
# text = TextBlob('''
# I do not like this car.
# This view is horrible.
# I feel tired this morning.
# I am not looking forward to the concert.
# He is my enemy.
# ''')

# print(text.sentiment)
