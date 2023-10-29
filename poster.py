from social_api import TwitterApi, InstagramAPI
from dotenv import load_dotenv
import yaml
import os

def get_message(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data
    except FileNotFoundError:
        print(f"YAML file not found: {file_path}")
        return {}
    except Exception as e:
        print(f"Error loading YAML file: {str(e)}")
        return {}

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
    content = "Hello, world! This is a test post."
    
    try:
        twitter_api.post(content)
        print("Tweet posted successfully on Twitter.")
    except Exception as e:
        print(f"Error posting on Twitter: {str(e)}")

    # INSTAGRAM
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')

    try:
        instagram_api = InstagramAPI(username, password)
        login_successful = instagram_api.login

        if login_successful:
            data = get_message('config.yaml')
            image_path = 'path/to/image'
            instagram_api.post(image_path, data)
            print("Image posted successfully on Instagram.")
        else:
            print("Instagram login failed.")
    except Exception as e:
        print(f"Error posting on Instagram: {str(e)}")

if __name__ == '__main__':
    data = get_message('config.yaml')
    print(data)
    poster()

