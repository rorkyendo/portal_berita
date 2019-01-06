"""
    Mengimport HttpResponse
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
    return render(request,'index.html')

"""
    Membuat def request ke about tanpa templating
"""
def about(request):
    return HttpResponse("<h1> ini adalah About</h1>")
