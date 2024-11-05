from django.contrib import admin
from django.template.defaulttags import comment

from .models import Article, ForumPost, Comment
# Register your models here.

admin.site.register(Article)
admin.site.register(ForumPost)
admin.site.register(Comment)
