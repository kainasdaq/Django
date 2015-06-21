# keyboards/models.py

from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles
from django.contrib.auth.models import User


class Keyboard(models.Model):
    # Create your models here.
    TYPE_M = 'M'
    TYPE_E = 'E'
    TYPE_CHOICES = (
        (TYPE_M, 'Mechanical'), 
        (TYPE_E, 'Electrostatic Capacitive'),
    )

    name = models.CharField( max_length = 50, default = 'Test_Keyboard' )
    type = models.CharField( max_length = 50, choices = TYPE_CHOICES, default = TYPE_M )
    color = models.CharField( max_length = 25, default = 'Black' )
    price = models.DecimalField( max_digits = 20, decimal_places = 2, default = 0.0)
    
    # ch.4 auth & permissions
    # fields = ( 'id', 'username', 'keyboards' ) from UserSerializer
    ### related_name must match fields name !!! ###
    owner = models.ForeignKey('auth.User', related_name = 'keyboards' )  
    highlighted = models.TextField(blank = True, default = '')
    
    class Meta:
        ordering = ['-price',]

    def __unicode__(self):
        return u'%s %s' % (self.name, self.color)
