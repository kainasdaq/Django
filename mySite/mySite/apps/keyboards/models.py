from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles

# Create your models here.
TYPE_CHOICES = (
    ('M', 'Mechanical'), 
    ('E', 'Electrostatic Capacitive')
)

class Keyboard(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='M')
    color = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    #class Meta:
    #    ordering = ['-price']

    def __unicode__(self):
        return u'%s %s' % (self.name, self.color)
