from django.urls import path, include
from simplemooc.forum import views as forum_views

app_name = 'forum'

urlpatterns = [
    path('', forum_views.index, name='index'),
    path('tag/<tag>', forum_views.index, name='index_tagged'),
    path('topico/<slug:slug>', forum_views.thread, name='thread'),
    path('respostas/<pk>/correta/', forum_views.reply_correct, name='reply_correct'),
    path('respostas/<pk>/incorreta/', forum_views.reply_incorrect, name='reply_incorrect'),



]
