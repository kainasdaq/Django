from django.shortcuts import render

# REST auth
from rest_framework import generics
from django.contrib.auth.models import User
from mySite.apps.token_demo.serializers import UserSerializer

# for REST JWT auth
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

# ====== REST auth ======
class UserList( generics.ListAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail( generics.RetrieveAPIView ):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ======= REST JWT auth ======
class RestrictedUserList(APIView):
    #permission_classes = ( IsAuthenticatedOrReadOnly, )
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( JSONWebTokenAuthentication, )
                
    def get( self, request, format = None ):
        serializer = UserSerializer( User.objects.all() , many = True )
        return Response( serializer.data )

    def post( self, request, format = None ):
        return self.get(request)
        '''
        serializer = UserSerializer( data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status.HTTP_201_CREATED )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )
        '''

class RestrictedUserDetail(APIView):
    #permission_classes = ( IsAuthenticatedOrReadOnly, )
    permission_classes = ( IsAuthenticated, )
    authentication_classes = ( JSONWebTokenAuthentication, )
                
    def get_object( self, pk ):
        try:
            return User.objects.get( pk = pk )
        except User.DoesNotExist:
            raise django.http.Http404

    def get( self, request, pk, format = None ):
        serializer = UserSerializer( self.get_object( pk )  )
        return Response( serializer.data )

    def put( self, request, pk, format = None ):
        return self.get( request, pk )
        '''
        serializer = UserSerializer( self.get_object( pk ), data = request.DATA )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )
        return Response( serializer.errors, status = status.HTTP_400_BAD_REQUEST )

    def delete( self, request, pk, format = None ):
        keyboard = self.get_object( pk )
        keyboard.delete()
        return Response( status = status.HTTP_204_NO_CONTENT )
        '''


