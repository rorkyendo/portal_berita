"""
    Mengimport dan membuat tampilan dengan HttpResponse
"""
from django.http import HttpResponse

"""
import templates yang diluar
"""
from django.shortcuts import render

#method view index
"""
    Membuat def request ke index dengan templating
"""
def index(request):
    context = {
        'judul' : 'Portal Berita',
        'nav' : [
            ['/','Home'],
            ['/portal','Portal'],
            ['/about','About'],
            ['/portal/recent','Recent']
        ],
        'subjudul':'Home'
    }
    content="content/index.html"
    return render(request,content,context)
