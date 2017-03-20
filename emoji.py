# 1000 recently streamed tweets should be in the file: "tweets"
import json, re

def clean_emoji_data(data):
    # Data is a list of tuples, where one element of the 5-tuple is an emoji
    # We just want a list of emojis
    flat_list = []
    for tuple in data:
        for item in tuple:
            if item != u'':
                flat_list += item
    return flat_list

tweetfile = open("tweets", "r")

numTweets = 0
for line in tweetfile:
    #print line.strip()
    tweet = json.loads(line.strip())
    
    #print json.dumps(tweet)
    try:
        #http://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
        emoji_data = re.findall(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", tweet['text'])

        # This gives us a weird format.
        #if len(m) >0:
        data = clean_emoji_data(emoji_data)
        print data
        numTweets += 1
    except:
        continue
    
tweetfile.close()
print("File reading complete. " + str(numTweets) + " tweets read.")
