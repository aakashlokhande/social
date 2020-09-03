from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='accounts'
urlpatterns = [
    path('',views.home,name='accounts_home'),
    path('register',views.register,name='register'),
    path('profile/',views.red_profile, name='red_profile'),
    path('profile/<int:id>',views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name ='accounts/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    
]