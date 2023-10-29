import unittest
from unittest.mock import MagicMock
from social_api import TwitterApi

class TestTwitterApi(unittest.TestCase):


    def test_credentials(self):
        pass

    def test_post(self):
        # Mock the Tweepy API
        mock_api = MagicMock()
        twitter_api = TwitterApi(
            client_key='client_key',
            client_secret='client_secret',
            access_token='access_token',
            access_token_secret='access_token_secret'
        )
        twitter_api.api = mock_api  

        # Call the post method
        content = "Test tweet content"
        twitter_api.post(content)

        mock_api.update_status.assert_called_once_with(status=content)

if __name__ == '__main__':
    unittest.main()
