from django.urls import path
from . import views


app_name='features'
urlpatterns = [
    path('users',views.users, name='users'),
    path('suggestions',views.suggestions, name='suggestions'),
    path('news',views.news, name='news'),
    path('announcement',views.announcement, name='announcement'),
]