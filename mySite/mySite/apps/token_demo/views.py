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
    permission_classes = ( IsAuthenticatedOrReadOnly, )
    authentication_classes = ( JSONWebTokenAuthentication, )
                
    def get(self, request):
        data = {}
        return Response(data)

class RestrictedUserDetail(APIView):
    permission_classes = ( IsAuthenticatedOrReadOnly, )
    authentication_classes = ( JSONWebTokenAuthentication, )
                
    def get(self, request):
        data = {}
        return Response(data)
