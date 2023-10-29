import facebook

class FacebookAPI:
    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token)
    
    def post(self, message):
        try:
            self.graph.put_object("me", "feed", message=message)
            print("Posted to Facebook successfully.")
        except facebook.GraphAPIError as e:
            print(f"Error posting to Facebook: {str(e)}")
