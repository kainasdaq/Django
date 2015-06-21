# mySite/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User

from mySite.apps.keyboards.models import Keyboard

class UserSerializer( serializers.ModelSerializer ):
    # queryset arg is also a must, only using 'many = True' doesn't work here
    keyboards = serializers.PrimaryKeyRelatedField( many = True, queryset = Keyboard.objects.all() ) # queryset arg is a must

    class Meta:
        model = User
        fields = ( 'id', 'username', 'keyboards' )
