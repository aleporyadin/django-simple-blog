from django.shortcuts import render 
from newsapi import NewsApiClient 
import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def news_bbc(request): 
    
    newsapi = NewsApiClient(api_key ='ae9cdcd03c374a4d8bdd829cea3408cc') 
    news_bcc = newsapi.get_top_headlines(sources ='techcrunch') 
  
    articles = news_bcc['articles'] 
    descriptions_n =[] 
    titles_n =[] 
    images_n =[] 
    sources_n =[]
    for i in range(len(articles)): 
        myArticle = articles[i] 
        titles_n.append(myArticle['title']) 
        temp = myArticle['description']
        if(len(temp)>=165):
            temp = temp[0:100:1]
        descriptions_n.append(temp)
        temp =""
        images_n.append(myArticle['urlToImage']) 

        temp = myArticle['publishedAt']
        temp = temp[:10:1]
        #dates_n.append(temp)

        sources_n.append(myArticle['url'])

    mylist = zip(titles_n, descriptions_n, images_n,sources_n) 

    return render(request, 'news/news.html', context ={"news_data_list":mylist}) 



def news_techcrunch(request): 
      
    newsapi = NewsApiClient(api_key ='ae9cdcd03c374a4d8bdd829cea3408cc') 
    news_techcrunch = newsapi.get_top_headlines(sources ='techcrunch') 
  
    articles = news_techcrunch['articles'] 
    descriptions_n =[] 
    titles_n =[] 
    images_n =[] 
    dates_n=[]
    sources_n =[]
    for i in range(len(articles)): 
        myArticle = articles[i] 
        titles_n.append(myArticle['title']) 
        descriptions_n.append(myArticle['description']) 
        images_n.append(myArticle['urlToImage']) 

        temp = myArticle['publishedAt']
        temp = temp.split()
        dates_n.append(temp)

        sources_n.append(myArticle['url'])

    mylist = zip(titles_n, descriptions_n, images_n,dates_n,sources_n) 
  
    return render(request, 'news/news.html', context ={"news_data_list":mylist}) 

def news_detail(request):          
    return render(request, 'news/news_detail.html') 
