from __future__ import unicode_literals
from django.db import models


class Cypher(models.Model):
    cypher_text = models.CharField(max_length=400)
    decipher_text = models.CharField(max_length=400)