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
        'judul':'Portal Berita'
    }
    return render(request,'index.html',context)
