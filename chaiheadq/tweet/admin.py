from django.contrib import admin
from .models import Tweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display=('id', 'user', 'text', 'photo', 'created_at', 'updated_at')


admin.site.register(Tweet, TweetAdmin)
