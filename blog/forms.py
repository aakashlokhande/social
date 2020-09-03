from django import forms
from accounts.models import User
from .models import Post, Comment, Likes
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['title','content','snippet','thumbnail_img','author']
        exclude=('author',)

class CommentsForm(forms.ModelForm):

    class Meta:
         model= Comment
         fields=['comment','writer','post']
         exclude=('writer','post',)