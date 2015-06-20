from django.shortcuts import render, render_to_response
import psycopg2 # PostgreSQL

# for REST
from mySite.apps.keyboards.models import Keyboard
from mySite.apps.keyboards.serializers import KeyboardSerializer
from rest_framework import generics # form generics.ListCreateAPIView & RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

def db_keyboard(request):
    db = psycopg2.connect(user='kai', dbname='kai_db', password='zxcvbnm', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM keyboards_keyboard ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('keyboards/db_list.html', {'names': names})

# ====== RESTful ======
# function based views VS class based views

# --- keyboard list ---
@api_view(['GET', 'POST']) # function based view
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

class KeyboardList( APIView ): # class based view
    def get( self, request, format = None ):
        keyboards = Keyboard.objects.all()
        serializer = KeyboardSerializer( keyboards, many = True )
        return Response( serializer.data )

    def post( self, request, format = None ):
        serializer = KeyboardSerializer( data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status.HTTP_201_CREATED )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

class KeyboardList_2( generics.ListCreateAPIView ):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

# --- keyboard detail ---

@api_view(['GET', 'POST', 'DELETE']) # function based view
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
            return Response( serializer.data )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    elif request.method == 'DELETE':
        keyboard.delete()
        return Response( status = status.HTTP_204_NO_CONTENT )

class KeyboardDetail( APIView ): # class based view
    def get_object( self, pk ):
        try:
            return Keyboard.objects.get( pk = pk )
        except Keyboard.DoesNotExist:
            raise django.http.Http404

    def get( self, request, pk, format = None ):
        keyboard = self.get_object( pk )
        serializer = KeyboardSerializer( keyboard )
        return Response( serializer.data )

    def put( self, request, pk, format = None ):
        keyboard = self.get_object( pk )
        serializer = KeyboardSerializer( keyboard, data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    def delete( self, request, pk, format = None ):
        keyboard = self.get_object( pk )
        keyboard.delete()
        return Response( status = status.HTTP_204_NO_CONTENT )

class KeyboardDetail_2 ( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

