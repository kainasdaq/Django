from django.shortcuts import render, render_to_response
import psycopg2 # PostgreSQL

# for REST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mySite.apps.keyboards.models import Keyboard
from mySite.apps.keyboards.serializers import KeyboardSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

def db_keyboard(request):
    db = psycopg2.connect(user='kai', dbname='kai_db', password='zxcvbnm', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM keyboard ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('keyboards/db_list.html', {'names': names})

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def keyboard_list(request):
    if request.method == 'GET':
        keyboards = Keyboard.objects.all()
        serializer = KeyboardSerializer( keyboards, many = True )
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KeyboardSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse( serializer.data, status = 201 )

        return JSONResponse( serializer.errors, status = 400 )

def keyboard_detail(request, pk):
    try:
        keyboard = Keyboard.objects.get(pk = pk)
    except Keyboard.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == 'GET':
        serializer = KeyboardSerializer( keyboard )
        return JSONResponse( serializer.data )

    elif request.method == 'PUT':
        data = JSONParser().parse( request )
        serializer = KeyboardSerializer( keyboard, data = data )
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse( serializer.errors, status = 400 )

    elif request.method == 'DELETE':
        keyboard.delete()
        return HttpResponse( status = 204 )
