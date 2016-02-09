from __future__ import unicode_literals

# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from cardsGame.models.bundle_model import Bundle

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Card(models.Model):

    bundle = models.ForeignKey(Bundle, default='')
    image = models.URLField(blank=False, default='' )
    name = models.CharField(max_length=100, blank=False)
    power = models.IntegerField(blank=True, default='')


    class Meta:
        ordering = ('bundle',)
