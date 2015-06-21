# mySite/views.py

from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
import datetime

# REST auth
from rest_framework import generics
from django.contrib.auth.models import User
from mySite.serializers import UserSerializer

# =====================================================

def hello(request):
    context = {}
    context['hello'] = 'Hello world, Django'
    return render(request, 'hello.html', context)

def detail(request, my_args):
    return HttpResponse("Looking at my_args %s" % my_args)

def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    context = {}
    context['current_date'] = now
    return render(request, 'current_datetime.html', context)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    """ break point to check local var """
    # using 'assert False' as break point to check var values
    next_time = datetime.datetime.now() + datetime.timedelta(hours = offset)
    #html = "<html><body>In %s hour(s), it willl be %s.</body></html>" % (offset, next_time)
    context = {}
    context['hour_offset'] = offset
    context['next_time'] = next_time
    return render(request, 'hours_ahead.html', context) 

def order_confirmation(request):
    """
    context = {}
    context['customer_name'] = 'Kai'
    context['order_number'] = '110-4158206-7371406'
    context['item_list'] = {'Filco Ninja Majestouch-2','Cherry','CM Storm QuickFire'}
    context['express_delivery'] = True
    #return render(request, 'order_confirmation.html', context)
    return render_to_response('order_confirmation.html', context)
    """
    customer_name = 'Kai'
    order_number = '110-4158206-7371406'
    item_list = {'Filco Ninja Majestouch-2','Cherry','CM Storm QuickFire'}
    express_delivery = True
    # when using locals(), local variables' names must match those var in the template!
    #return render_to_response( 'order_confirmation.html', locals() )
    return render(request, 'order_confirmation.html', locals())

# REST auth
class UserList( generics.ListAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail( generics.RetrieveAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

