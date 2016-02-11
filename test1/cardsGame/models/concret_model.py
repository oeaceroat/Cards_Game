from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from cardsGame.models.bundle_model import Bundle

class Concret(models.Model):
    bundle = models.ForeignKey(Bundle, default='')


