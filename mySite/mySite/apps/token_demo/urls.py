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

from mySite.apps.token_demo import views

urlpatterns = [
    # auth.user 
    url(r'users-open/$', views.UserList.as_view()),
    url(r'users-open/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    
    # rest jwt auth
    url(r'api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    
    url(r'users-restricted/$', views.RestrictedUserList.as_view()),
    url(r'users-restricted/(?P<pk>[0-9]+)/$', views.RestrictedUserDetail.as_view()),
]
