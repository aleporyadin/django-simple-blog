from django.contrib import admin 
from django.urls import path 
from .views import (
    news_techcrunch, 
    news_bbc,
    news_detail
)
  
urlpatterns = [ 
    path('', news_bbc, name ='blog-news'), 
    path('tech/', news_techcrunch, name='news-techcrunch' ),
    path('detail/',    news_detail, name='news-detail')

] 