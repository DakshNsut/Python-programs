import requests
import json
from win32com.client import Dispatch
import datetime

date = datetime.date.today()

def voice_content(content):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(content)

def url_news(numb):
    if numb > len(dict):
        voice_content("That is an invalid headline number")
        return False
    return dict[numb]

# url = f"https://newsapi.org/v2/everything?q=jee&from={date}&sortBy=publishedAt&apiKey=22b199707b564ce08bda05624a45bfec"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=22b199707b564ce08bda05624a45bfec"
news = requests.get(url).text
news_dict = json.loads(news)
news_articles = news_dict['articles']
print("Press Enter to listen to News")
input()
dict = {}
voice_content("News for today is")
voice_content("Listen Carefully")

n=12
'''
for title in news_articles:
    news_title = title['title']
    voice_content(f"Headline{n}")
    voice_content(news_title)
    news_description = title['description']
    # voice_content(news_description)
    news_url = title['url']
    dict[n] = news_url
    n+=1
    continue
    '''

while n>1:
    voice_content("Do you want to know more about a particular headline? Enter Y or N:")
    response = input()
    if response == "N" or response == "n":
        break
    elif response == "Y" or response == "y":
        voice_content("Enter the number of that headline:")
        headline_number = int(input())
        url = url_news(headline_number)
        if url == False:
            continue
        voice_content("Click on the url below to know more.")
        print(url)

if(n == 1):
    voice_content("There were no articles on the given topic for the given day")
voice_content(".....Thanks for using my news headline speaker.")