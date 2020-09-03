from django.db import models
from django.utils import timezone
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Suggestion(models.Model):
    suggestion= models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class Announcement(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    announcement= RichTextUploadingField()
    date_posted= models.DateTimeField(default=timezone.now)

class News(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    content= RichTextUploadingField()
    date_posted= models.DateTimeField(default=timezone.now)