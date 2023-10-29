from social_api import TwitterApi
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
    twitter_api.post(content)
    
    
    #FACEBOOk 
    

    

if __name__ == '__main__':
    data = get_message('config.yaml') 
    print(data)
    poster()
