from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world, Django")

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
