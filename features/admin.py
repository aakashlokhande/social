from django.contrib import admin
from .models import Suggestion, News, Announcement
# Register your models here.

admin.site.register(Suggestion)
admin.site.register(News)
admin.site.register(Announcement)