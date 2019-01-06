from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Portal Berita'
    }
    return render(request,"portal.html",context)

def recent(request):
    context = {
        'judul':'Portal Berita'
    }
    return render(request,"recent.html",context)
