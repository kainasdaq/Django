from django.db import models

# Create your models here.
class Keyboard(models.Model):
    TYPE_CHOICES = (
        ('M', 'Mechanical'), 
        ('E', 'Electrostatic Capacitive')
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='M')
    color = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.color)
