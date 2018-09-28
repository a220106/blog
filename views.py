# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from  . import models

def index(request):

    articles = models.Article.objects.all()
    return render(request, 'index.html' ,{'articles':articles})
def artic_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return  render(request,'blog/article_page',{'article',article})
# Create your views here.
