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

tweetfile = open("tweetswithrts", "r")
emojidata = open ("emojidata", "w")
numTweets = 0
infoArray = []
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

        data_entry = [data]
        if tweet.has_key('retweeted_status'):
            count = tweet['retweet_count']
        else:
            count = 0
            
        
        infoArray += [[data, count]]

        numTweets += 1
    except:
        continue

for info in infoArray:
    emojis = info[0]
    retweets = info[1]
    emojiCount = str(len(emojis))
    emojidata.write(emojiCount + ' ')
    print emojiCount
    retweetCount = str(retweets)
    emojidata.write(retweetCount + '\n')
    print retweetCount
tweetfile.close()
emojidata.close()
print("File reading complete. " + str(numTweets) + " tweets read.")
