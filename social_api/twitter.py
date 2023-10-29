import tweepy

class TwitterApi:
    def __init__(self, client_key, client_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(client_key, client_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def post(self, content):
        self.api.update_status(status=content)