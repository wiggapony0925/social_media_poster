from social_api import TwitterApi
from dotenv import load_dotenv
import os

def poster():
    load_dotenv()
    
    # TWITTER
    twitter_credentials = {
        "client_key": os.getenv('TWITTER_CLIENT_KEY'),
        "client_secret": os.getenv('TWITTER_CLIENT_SECRET'),
        "access_token": os.getenv('TWITTER_ACCESS_TOKEN'), 
        "access_token_secret": os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
    }
    
    twitter_api = TwitterApi(**twitter_credentials)
    
    # Create a post
    content = "Hello, world! This is a test post."
    twitter_api.post(content)

if __name__ == '__main__':
    poster()
