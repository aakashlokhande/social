from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone
from accounts.models import User

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=100,null=True, blank=True)
    content=RichTextUploadingField()
    date_posted=models.DateTimeField(default=timezone.now)
    snippet=RichTextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail_img= models.ImageField(upload_to='post_pics')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment= models.TextField()
    date_posted=models.DateTimeField(default= timezone.now)
    writer= models.ForeignKey(User, on_delete= models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} {self.pk}'

class Likes(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_users=models.ManyToManyField(User, related_name='liked_users', blank=True)

    def __str__(self):
        return f'{self.post} {self.pk}'