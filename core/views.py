from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from .models import Article, ForumPost
# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, 'core/home.html', {'articles':articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article)
    return render(request, 'core/article_detail.html', {'article':article}, context)

def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'core/forum.html', {'posts',posts})


