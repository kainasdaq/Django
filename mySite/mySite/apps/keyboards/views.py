from django.shortcuts import render, render_to_response
import psycopg2 # PostgreSQL

# for REST
from mySite.apps.keyboards.models import Keyboard
from mySite.apps.keyboards.serializers import KeyboardSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def db_keyboard(request):
    db = psycopg2.connect(user='kai', dbname='kai_db', password='zxcvbnm', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM keyboards_keyboard ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('keyboards/db_list.html', {'names': names})
'''
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
'''
@api_view(['GET', 'POST'])
def keyboard_list(request, formate = None):
    if request.method == 'GET':
        keyboards = Keyboard.objects.all()
        serializer = KeyboardSerializer( keyboards, many = True )
        return Response( serializer.data )

    elif request.method == 'POST':
        serializer = KeyboardSerializer( data = request.DATA )

        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status = status.HTTP_201_CREATED )

        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

@api_view(['GET', 'POST', 'DELETE'])
def keyboard_detail(request, pk, format = None):
    try:
        keyboard = Keyboard.objects.get(pk = pk)
    except Keyboard.DoesNotExist:
        return Response( status = status.HTTP_404_NOT_FOUND )

    if request.method == 'GET':
        serializer = KeyboardSerializer( keyboard )
        return Response( serializer.data )

    elif request.method == 'PUT':
        serializer = KeyboardSerializer( keyboard, data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        keyboard.delete()
        return HttpResponse( status = status.HTTP_204_NO_CONTENT )
