from __future__ import unicode_literals

# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from cardsGame.models.concret_model import Concret
from cardsGame.models.card_form_model import CardForm

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class ConcretCard(Concret):
    form = models.ForeignKey(CardForm)
    locked = models.BooleanField(null=False, default=False)
