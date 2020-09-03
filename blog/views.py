from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, FileResponse, JsonResponse
from accounts.models import User
from .forms import PostForm, CommentsForm
from .models import Post, Comment, Likes
from django.utils import timezone
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    else:
        return render(request, 'blog/index.html')

def home(request):
    posts= Post.objects.all().order_by('-date_posted')

    return render(request, 'blog/home.html',{'posts':posts})

def create_post(request):
    if request.method=='POST':
        form =PostForm(request.POST, request.FILES)
        if form.is_valid:
            inst= form.save(commit=False)
            inst.author= request.user
            inst.save()
            Likes.objects.create(post=inst)
            return redirect('blog:home')
    
    else:
        form= PostForm()

    return render(request,'blog/create_post.html',{'form':form})

def post_detail(request, id):
    post = Post.objects.filter(pk=id).first()
    comments= Comment.objects.filter(post=post)
    if comments == None:
        comments=[]
    else:
        comments=comments.all().order_by('-date_posted')
    
    likes= Likes.objects.filter(post=post).first()
    form= CommentsForm()

    return render(request, 'blog/post_detail.html',{'post':post, 'comments':comments,'likes':likes, 'form':form})

def create_comment(request):
    writer=request.user
    id= request.POST['id']
    if request.method=="POST":
        form=CommentsForm(request.POST)
        
        if form.is_valid:
            inst=form.save(commit=False)
            post= Post.objects.filter(pk=id).first()
            inst.post=post
            inst.writer=writer
            inst.save()
        
            return JsonResponse({'date_posted':inst.date_posted, 'comment':str(request.POST['comment'])})
        else:
            return JsonResponse({'done':False}) 

def like_post(request):
    id=int(request.POST['like_id'])
    
    email=request.POST['like_email']
    user=User.objects.filter(email=email).first()
    user_pk=user.pk
    
    post=Post.objects.filter(pk=id).first()
    like_object= Likes.objects.filter(post=post).first()
    liked_users= like_object.liked_users.all()
    trig=0
    for person in liked_users:
        if person==user:
            trig=1
    if trig==0:
        num=len(list(liked_users))
        like_object.liked_users.add(user_pk)
        like_object.save()
        return JsonResponse({'message':f'{user.first_name} {user.last_name} and {num} others'})

    else:
        like_object.liked_users.remove(user_pk)
        like_object.save()
        num=len(list(liked_users))-1
        if num==0:
            return JsonResponse({'message':f'0 likes'})
        else:
            return JsonResponse({'message':f'{liked_users[0].first_name} {liked_users[0].last_name} and {num-1} others'})



    