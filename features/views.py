from django.shortcuts import render, redirect
from accounts.models import User
from .models import Suggestion, News, Announcement
from .forms import SuggestionsForm

# Create your views here.
def users(request):
    users=User.objects.all()

    return render(request,'features/users.html',{'users':users})

def suggestions(request):

    if request.method=='POST':
        form= SuggestionsForm(request.POST)
        if form.is_valid:
            inst=form.save(commit=False)
            inst.user=request.user
            inst.save()

        return redirect('blog:home')
    else:
        form=SuggestionsForm()

    return render(request,'features/suggestions.html',{'form':form})

def news(request):
    news_list=News.objects.all()
    exists=False
    if len(news_list)>0:
        exists=True
    return render(request, 'features/news.html',{'news_list':news_list,'exists':exists})

def announcement(request):
    announcements=Announcement.objects.all()
    exists=False
    if len(announcements)>0:
        exists=True
    return render(request, 'features/announcements.html',{'announcements':announcements,'exists':exists})