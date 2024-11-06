from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, ForumPost
from .forms import RegistrationForm
# Create your views here.

def home(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'core/home.html', context)

def post(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'core/post.html', context)


def article_detail(request):
    article = get_object_or_404(Article)
    context = {'article': article}
    return render(request, 'core/article_detail.html',context)

def forum(request):
    posts = ForumPost.objects.all()
    context = {'posts',posts}
    return render(request, 'core/forum.html', context)


def signup(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render("core:home")
    else:
        form = RegistrationForm

    context = {"form": form}
    return render(request, "core/signup.html", context)