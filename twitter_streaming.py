from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "744844861308706816-VbhoIz17IOxwObqomGsgYUamqkwqBII"
access_token_secret = "MkEEEMpUZngSfq7qIGGpUu2NvVt2Jfno9IwAsINFSSweZ"
consumer_key = "X95sViWOgF4CDGEmqeL6H27Nz"
consumer_secret = "mCutrtH1jtIOmbpEFQJDk33HX7OBN1Y2D07z4OFwVGv3MaWGtX"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

stream.filter(track=['hillary clinton', 'donald trump'])