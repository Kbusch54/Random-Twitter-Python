import tweepy
cfg={
    "consumer_key":('.env'),
    "consumer_secret":('.env'),
    "bearer_token":('.env'),
    "access_token":('.env'),
    "access_token_secret":('.env'),
}

def get_client(cfg):
    try:
        client = tweepy.Client(cfg['bearer_token'])
        print("client Success")
        print(client)
        return client
    except:
        print("Error: Authentication Failed")
        return None
        # api = tweepy.API(auth, wait_on_rate_limit=True)
        # auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        # auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])



def get_tweets(username):
    api = get_api_handler(cfg)
    tweets = tweepy.Cursor(api.user_timeline(screen_name=username))
    return tweets
def get_following(api, user):
        following = []
        for page in api.get_list_followers(user, count=2):
            following.extend(page)
        return following

def get_api_handler(cfg):
    try:
        client = tweepy.Client(
            bearer_token=cfg['bearer_token'], 
            consumer_key=cfg['consumer_key'], 
            consumer_secret=cfg['consumer_secret'], 
            access_token=cfg['access_token'], 
            access_token_secret=cfg['access_token_secret'])
        print("Authentication Success")
        return client
    except:
        print("Error: Authentication Failed")
        return None
    
if(__name__ == '__main__'):
    client = get_api_handler(cfg)
    print(client)
    followers = client.get_users_followers(id=53836928, max_results=10)
    print(followers)