from django.http import HttpResponse, Http404
from django.shortcuts import render

import datetime

def hello(request):
    context = {}
    context['hello'] = 'Hello world, Django'
    return render(request, 'hello.html', context)

def detail(request, my_args):
    return HttpResponse("Looking at my_args %s" % my_args)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    """ break point to check local var """
    #assert False
    ha = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it willl be %s.</body></html>" % (offset, ha)
    return HttpResponse(html)

def order_confirmation(request):
    context = {}
    context['customer_name'] = 'Kai'
    context['order_number'] = '110-4158206-7371406'
    context['item_list'] = {'Filco Ninja Majestouch-2','Cherry','CM Storm QuickFire'}
    context['express_delivery'] = True
    return render(request, 'order_confirmation.html', context)
