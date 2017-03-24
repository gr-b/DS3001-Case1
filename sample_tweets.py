import twitter, json

# Define a Function to Login Twitter API
def get_oauth_login():
    # Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information 
    # on Twitter's OAuth implementation.
    
    CONSUMER_KEY = '6wqmAA369v9LKAM1iEEmworfI'
    CONSUMER_SECRET ='ZpGKzYbc9BGKyarLtrcg8DVpiYjbsAww7v2fgr0eres2r1vgUN'
    OAUTH_TOKEN = '842787201540915202-9HyTDqDstoubiShHeNxA6tk5CPY0vvG'
    OAUTH_TOKEN_SECRET = 'b2sKJWNi4nq1gfJo5Twqwb3H8HPwh14yzJ3lpfCUWXKYb'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    #twitter_api = twitter.Twitter(auth=auth)
    return auth

#print oauth_login()

#----------------------------------------------
# Your code starts here
#   Please add comments or text cells in between to explain the general idea of each block of the code.
#   Please feel free to add more cells below this cell if necessary

# Only collect data on the northeast
# https://dev.twitter.com/docs/api/1.1/get/trends/place
# http://developer.yahoo.com/geo/geoplanet/

auth = get_oauth_login()
twitter_stream = twitter.TwitterStream(auth=get_oauth_login())
iterator = twitter_stream.statuses.sample()
#twitter_obj = twitter.Twitter(auth=auth)
#iterator = twitter_obj.search.tweets(count=1000)

count = 50000
tweetfile = open("tweets6","w")

for tweet in iterator:
    count += -1
    tweetfile.write(json.dumps(tweet) + "\n")

    if count <=0:
        break

tweetfile.close()
