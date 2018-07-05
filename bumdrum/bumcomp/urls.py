from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    path('box/<away>/<home>/<int:date>',  views.boxscore, name='boxscore'),
    path('boxscore/<away>/<home>/<int:date>',  views.boxscore, name='boxscore'),
    path('json/pbp/<away>/<home>/<int:date>',views.pbp_json, name='pbp_json'),
]
