# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Index page reached</h1>')
    context={
        'name':'Justin',
        'gender':'male'
    }
    return render(request, 'index.html', context)