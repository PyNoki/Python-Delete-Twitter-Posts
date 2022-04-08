import time
import json
import tweepy

# assign the values accordingly
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""
user_name = '' #Your @Username

# Start Loop

while True:
    # authorization of api key and api secret
    auth = tweepy.OAuthHandler(api_key, api_secret)

    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)

    # calling the api 
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    #Get json data - Set your @username
    json_data = api.user_timeline(screen_name=user_name)
    data = json.dumps(json_data)
    parsed = json.loads(data)

    for item in parsed:
        postID = item.get("id")
        print(postID)
        api.destroy_status(id=postID)
        time.sleep(0.5)
