from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.conf import settings
from django.http import HttpResponse, FileResponse, JsonResponse
from .models import User
from blog.models import Post

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def register(request):

    if request.method=='POST':
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid :
            form.save()
            return redirect('blog:index')

    else:
        form=UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form':form})

def red_profile(request):
    id=request.user.pk
    return redirect('accounts:profile', id)

def profile(request,id):
    person=User.objects.filter(pk=id).first()
    posts= Post.objects.filter(author=person)
    if posts==None:
        posts=[]
    else:
        posts=posts.all()

    return render(request,'accounts/profile.html',{'person':person,'posts':posts})