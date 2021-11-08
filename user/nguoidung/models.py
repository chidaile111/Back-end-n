from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateField
import datetime
from django_countries.fields import CountryField

# Create your models here.
class RoomChat(models.Model):
    RoomID = models.CharField(max_length=4)
    def __str__(self):
        return self.RoomID

class User(models.Model):
    name = models.CharField(max_length=69)
    nation = CountryField()
    dateofbirth = models.DateField(default=datetime.date.today)
    email = models.EmailField(null=True)
    GENDER_CHOICES = (
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    RoomChat = models.ForeignKey(RoomChat, on_delete=PROTECT, default='', null=True)
    
    def __str__(self):
        return self.name