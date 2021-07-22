from gtts import gTTS
from playsound import playsound
import requests
import os
from api_cred import news_api as cred


# fetch the news
r = requests.get(
    f'https://newsapi.org/v2/top-headlines?country=in&apiKey={cred}')

# convert to json format
p = r.json()
count = p["totalResults"]

# pass to read out function
for i in range(count):
    mytext = p["articles"][i]["title"]

    if (p["articles"][i]["description"] != None):
        mydesc = p["articles"][i]["description"]

    news = mytext + mydesc

    language = 'en'
    myobj = gTTS(text=news, lang=language, slow=False)
    myobj.save(f"welcome{i}.mp3")
    playsound(f"welcome{i}.mp3")

    os.remove(f"welcome{i}.mp3")
