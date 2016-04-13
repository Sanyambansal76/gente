from django.conf.urls import patterns, include, url
from genteai import views

urlpatterns = patterns('',

    url(r'^$', views.gente, name='gente'),
    url(r'^send-message/', views.gente_reply, name='gente_reply'),
)
