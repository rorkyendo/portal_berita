from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.

"""
    Membuat def request ke about tanpa templating
"""
def about(request):
        context = {
            'judul' : 'Portal Berita',
            'nav' : [
                ['/','Home'],
                ['/portal','Portal'],
                ['/about','About'],
                ['/portal/recent','Recent']
            ],
            'subjudul':'About Us'
        }
        content="content/about.html"
        return render(request,content,context)
