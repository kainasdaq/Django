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

from mySite import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.hello),
    url(r'^hello/$', views.hello),
    url(r'^detail/(?P<my_args>\d{1,2})/$', views.detail, name = 'detail'),
    url(r'^time/$', views.current_datetime, name='time'),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead, name = 'time_plus'),
    url(r'^order/$', views.order_confirmation),

    url(r'^keyboards/', include('mySite.apps.keyboards.urls')),
    
    # auth.user 
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    # rest auth
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    # rest jwt auth
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
]
