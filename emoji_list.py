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

tweetfile = open("tweets5", "r")
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
            
        
        infoArray += [data]

        numTweets += 1
    except:
        continue

tweetfile.close()
print("File reading complete. " + str(numTweets) + " tweets read.")

tweets = []
for info in infoArray:
    emojiarr = []
    emojistr = u''
    i = 0
    for char in info:
        emojistr += char
        i += 1
        if i %2 == 0 and not i == 0:
            emojiarr += [emojistr[-2:]]
    tweets += [emojiarr]
    
dict = {}
for tweet in tweets:
    for emoji in tweet:
        for emoji2 in tweet:
            if not dict.has_key(emoji):
                dict[emoji] = {}
            
            if dict[emoji].has_key(emoji2) and not emoji == emoji2:
                dict[emoji][emoji2] += 1
            else:
                dict[emoji][emoji2] = 1

# clean dictionary. Remove entries below average
for key, value in dict.items():
    sum = 0
    for key2, value in dict[key].items():
        sum += value
    avg = int(sum/len(dict[key].items()))
    dict[key]['avg'] = avg
    dict[key]['Frequency'] = sum
    for key2, value in dict[key].items():
        if value <= avg:
            dict[key].pop(key2, None)
            if len(dict[key]) == 0:
                dict.pop(key, None)
            #print 'pooped'
            

def printInnerDict(innerDict):
    for emoji, num in sorted(innerDict.items()[:5], key= lambda x: x[1], reverse=True):
        if not emoji == 'Frequency':
            print '&nbsp;'*4 + emoji + '->' + str(num) + '<br>\n'

#Sort the dictionary by frequency
sortDict = sorted(dict.items(), key= lambda x: x[1]['Frequency'], reverse=True)
#print sortDict
    
    
for key, value in sortDict:
    print key + ":<br>\n"
    printInnerDict(dict[key])
    #for key2, value in dict[key].items():
        #print '&nbsp;'*4 + key2 + "->" + str(value) + '<br>\n'
    print '<br>'*2
