# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class music(models.Model):
    title=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    release=models.DateField(auto_now=False, auto_now_add=True)
    image=models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=['-release']
