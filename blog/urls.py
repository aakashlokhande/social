from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='blog'
urlpatterns = [
    path('',views.index, name='index'),
    path('home', views.home, name='home'),
    path('create_post',views.create_post, name='create_post'),
    path('post/<int:id>', views.post_detail, name='post_detail'),
    path('create_comment', views.create_comment, name='create_comment'),
    path('like_post', views.like_post, name='like_post'),

]