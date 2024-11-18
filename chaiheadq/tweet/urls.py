from . import views 
from django.urls import path


urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('tweet_list/', views.tweet_list, name='tweet_list'),

    path('tweet_create', views.tweet_create, name='tweet_create'),
    path('edit/<int:tweet_pk>', views.tweet_edit, name='tweet_edit'),
    path('delete/<int:tweet_pk>', views.tweet_delete, name='tweet_delete'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),

] 