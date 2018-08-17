from textblob import TextBlob
import base64 pprint requests
from keys import client_key
from keys import client_secret

key_secret = "{}:{}".format(client_key, client_secret).encode("ascii")
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

tweet_data = []

def get_tweet_ids_and_text(data):
    tweet_dict = {}
    for x in data:
        tweet_dict[x["id"]] = x["text"]
    return tweet_dict


def get_tweets():
    tweet_counter = 0
    max_id = None
    while tweet_counter < 1000:
        search_url = "{}1.1/search/tweets.json".format(base_url)
        search_params = {
            "q": "Trump hate bastard fucking",
            "result_type": "recent",
            "lang": "en",
            "count": 100,
            "max_id": max_id
        }
        search_resp = requests.get(search_url, headers=search_headers, params=search_params)    
        tweets_json = search_resp.json()
        tweet_info = tweets_json["statuses"]
        for x in tweet_info:
            tweet_data.append(x)
        # get lowest id from tweet data
        tweet_ids = []
        for x in tweets_json["statuses"]:
            tweet_ids.append(x["id"])
            lowest_id = tweet_ids[0]
            for id in tweet_ids:
                if id < lowest_id:
                    lowest_id = id
        max_id = lowest_id - 1
        tweet_counter += 100


get_tweets()
# pull out text and id from tweet data
processed_tweet_data = get_tweet_ids_and_text(tweet_data)

# remove all duplicate tweets
unique_tweets = {}
for tweet in processed_tweet_data:
        if tweet not in unique_tweets:
            unique_tweets[tweet] = processed_tweet_data[tweet]

# create a list of tweet text
tweet_texts = ""
for key in unique_tweets.values():
    tweet_texts += key

text = TextBlob(" ".join(tweet_texts))

print(text.sentiment)
