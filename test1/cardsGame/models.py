from __future__ import unicode_literals

# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class User(models.Model):
    
    name = models.CharField(max_length=100, blank=False)
    userName = models.CharField(max_length=100, blank=False)	
     	
    class Meta:
        ordering = ('name',)


class Player(models.Model):
    
    user = models.ForeignKey(User)
    acc_name = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('user',)


class Card(models.Model):

    player = models.ForeignKey(Player)
    image = models.URLField(null=True)
    name = models.CharField(max_length=100, blank=False, default='')
    power = models.IntegerField(blank=True, null=True)


    class Meta:
        ordering = ('player',)




    
    

