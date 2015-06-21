# keyboards/serializers.py

from rest_framework import serializers
from mySite.apps.keyboards.models import Keyboard

# =======================================================

class KeyboardSerializer(serializers.ModelSerializer):
    '''
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    type = serializers.ChoiceField(choices=TYPE_CHOICES, default='M') # ChoiceField
    color = serializers.CharField(max_length=25)
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    '''
    owner = serializers.ReadOnlyField( source = 'owner.username' )

    class Meta:
        model = Keyboard
        fields = ( 'id', 'name', 'type', 'color', 'price', 'owner' )
   
    '''
    def create(self, validated_data):
        return Keyboard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.color = validated_data.get('color', instance.color)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    '''

