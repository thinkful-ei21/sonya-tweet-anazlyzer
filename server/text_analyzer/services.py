from textblob import TextBlob
import base64, pprint, requests
from .keys import client_key
from .keys import client_secret


class Analyzer:

    def __init__(self):
        self.base_url = "https://api.twitter.com/"
        self.auth_url = "{}oauth2/token".format(self.base_url)
        self.key_secret = "{}:{}".format(client_key, client_secret).encode("ascii")
        self.b64_encoded_key = base64.b64encode(self.key_secret)
        self.b64_encoded_key = self.b64_encoded_key.decode("ascii")
        self.auth_headers = {
        "Authorization": "Basic {}".format(self.b64_encoded_key),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
        self.auth_data = {
        "grant_type": "client_credentials"
        }
        self.auth_resp = requests.post(self.auth_url, headers=self.auth_headers, data=self.auth_data)
        self.access_token = self.auth_resp.json()["access_token"]
        self.search_headers = {
        "Authorization": "Bearer {}".format(self.access_token)
        }
        self.tweet_data = []




    def get_tweet_ids_and_text(self, data):
        tweet_dict = {}
        for x in data:
            # pprint.pprint(x)
            tweet_dict[x["id"]] = x["text"]
        return tweet_dict


    def get_tweets(self, search_term):
        tweet_counter = 0
        max_id = None
        while tweet_counter < 1000:
            search_url = "{}1.1/search/tweets.json".format(self.base_url)
            search_params = {
                "q": "{}".format(search_term),
                "result_type": "recent",
                "lang": "en",
                "count": 10,
                "max_id": max_id
            }
            search_resp = requests.get(search_url, headers=self.search_headers, params=search_params)    
            tweets_json = search_resp.json()
            tweet_info = tweets_json["statuses"]
            for x in tweet_info:
                self.tweet_data.append(x)
            # get lowest id from tweet data and pass to api call as max_id param to get new tweets
            # loops through tweets and add id to the array if it is unique
            tweet_ids = []
            for x in tweets_json["statuses"]:
                if x["id"] not in tweet_ids:
                    tweet_ids.append(x["id"])

            # loop through tweet ids array and find lowest id number
            lowest_id = tweet_ids[0]
            for id in tweet_ids:
                if id < lowest_id:
                    # print('id: ',id, 'lowest id: ',lowest_id)
                    lowest_id = id
            # set the lowest id to the mas_id variable,
            max_id = lowest_id - 1
            tweet_counter += 100

    def analyze_tweets(self, search_term):


        self.get_tweets(search_term)
        # pull out text and id from tweet data
        processed_tweet_data = self.get_tweet_ids_and_text(self.tweet_data)

        # remove all duplicate tweets
        # unique_tweets = {}
        # for tweet in processed_tweet_data:
        #         # if tweet not in unique_tweets:
        #     unique_tweets[tweet] = processed_tweet_data[tweet]
        # print("----",unique_tweets,"------")
        # # create a list of tweet text
        tweet_texts = ""
        for key in processed_tweet_data.values():
            tweet_texts += key
            # print(key, " --- ")
        text = TextBlob(" ".join(tweet_texts))

        print(text.sentiment)
        return text.sentiment


# test = analyzer()

# test.analyze_tweets("have a great day happy")