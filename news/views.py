from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    #init the news api 
    NewsApi = NewsApiClient(api_key = '49ac8a649aed4ec69481c89777f257c0')
    headlines = NewsApi.get_top_headlines(sources='bbc-news')
    articles = headlines['articles']
    #get the news 
    des = []
    news = []
    img = []
    
    #get each article descriptions 
    for i in range(len(articles)):
        article =articles[i]
        des.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    myNews = zip(news,des,img)
    
    return render(request,'index.html',context={"myNews":myNews})

