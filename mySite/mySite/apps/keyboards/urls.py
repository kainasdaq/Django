"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from mySite.apps.keyboards import views
# https://docs.djangoproject.com/en/1.8/topics/http/urls/
urlpatterns = [
    url( r'^$', views.db_keyboard ),
    #url( r'^keyboards_list/$', views.keyboard_list ),
    #url( r'^keyboards_detail/(?P<pk>[0-9]+)/$', views.keyboard_detail ),
    
    #url( r'^keyboards_list_1/$', views.KeyboardList.as_view() ),
    #url( r'^keyboards_detail_1/(?P<pk>[0-9]+)/$', views.KeyboardDetail.as_view() ),
    
    url( r'^keyboards_list/$', views.KeyboardList.as_view() ),
    url( r'^keyboards_detail/(?P<pk>[0-9]+)/$', views.KeyboardDetail.as_view() ),
]
