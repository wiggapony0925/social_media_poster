import unittest
from unittest.mock import MagicMock
from social_api.facebook import FacebookAPI

class TestFacebookAPI(unittest.TestCase):
    
    def test_credentials(self):
        facebook_api = FacebookAPI(access_token='access_token')
        self.assertEqual(facebook_api.graph.access_token, 'access_token')
    
    def test_post(self):
        mock_api = MagicMock()
        facebook_api = FacebookAPI(access_token='access_token')
        facebook_api.graph = mock_api 
        
        content = 'this is a test to the Facebook API'
        facebook_api.post(content)
        
        mock_api.put_object.assert_called_once_with(parent_object='me', connection_name='feed', message=content)

if __name__ == '__main__':
    unittest.main()
