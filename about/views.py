from django.shortcuts import render

# Create your views here.

"""
    Membuat def request ke about tanpa templating
"""
def about(request):
    return render(request,"about.html")
