# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Portal Berita',
        'nav' : [
            ['/','Home'],
            ['/portal','Portal'],
            ['/about','About'],
            ['/portal/recent','Recent']
        ],
        'subjudul' : 'Portal Berita'
    }
    content="content/portal.html"
    return render(request,content,context)

def recent(request):
    context = {
        'judul' : 'Portal Berita',
        'nav' : [
            ['/','Home'],
            ['/portal','Portal'],
            ['/about','About'],
            ['/portal/recent','Recent']
        ],
        'subjudul': 'Recent Post'
    }
    content="content/recent.html"
    return render(request,content,context)
