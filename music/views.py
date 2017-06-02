# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import music
from .forms import musicForm

# Create your views here.
def index(request):
    #instance=music.objects.get(id=55)

    queryset=music.objects.all()
    #return HttpResponse('<h1>Index page reached</h1>')
    context={
        'title':'All Posts',
        'objList':queryset,
    }
    return render(request, 'base.html', context)

def detail(request, id=None):
    instance = get_object_or_404(music, id=id)

    # return HttpResponse('<h1>Index page reached</h1>')
    context = {
        'title':instance.title,
        'instance': instance,
    }
    return render(request, 'detail.html', context)


def create(request):
    form=musicForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance=form.save(commit=False)
        #print form.cleaned_data.get("title")
        instance.save()
        return redirect("list")

    # if request.method=="POST":
    #     print request.POST.get("artist")
    #     print request.POST.get("title")
    context={
        "form":form,
    }

    return render(request,'post_form.html',context)


def update(request, id=None):
    instance = get_object_or_404(music, id=id)
    form = musicForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        str='/posts/'+id
        return HttpResponseRedirect(str)

    context = {
        'title':instance.title,
        'instance': instance,
        "form":form,
    }
    return render(request, 'post_form.html', context)

def delete(request, id=None):
    instance = get_object_or_404(music, id=id)
    instance.delete()
    return redirect("list")
