# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import music

class musicModelAdmin(admin.ModelAdmin):
    class Meta:
        model=music
    list_display = ["title","artist","release"]
    search_fields = ["title"]


admin.site.register(music,musicModelAdmin)