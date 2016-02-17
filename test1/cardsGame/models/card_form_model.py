from __future__ import unicode_literals

# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from cardsGame.models.card_model import Card

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class CardForm(models.Model):
    card = models.ForeignKey(Card)
    name = models.CharField(max_length=100, blank=False,
                             null=False, default='new card form')
    num_levels = models.IntegerField(blank=False, null=False,default=0)
    form_sequence = models.IntegerField(blank=False, null=False,default=0)
    image = models.URLField(blank=False, default='', null=False )