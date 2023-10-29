from instabot import Bot

class InstagramAPI:
    def __init__(self, username, password):
        self.bot = Bot()
        self.username = username
        self.password = password
        self.login = self.bot.login(username=self.username, password=self.password)
        
    def post(self, image, content):
        self.bot.upload_photo(image, caption=content)
