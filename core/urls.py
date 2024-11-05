from django.urls import path
from .import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/int:article/', views.article_detail, name='article_detail'),
    path('forum/', views.forum, name='forum'),

]