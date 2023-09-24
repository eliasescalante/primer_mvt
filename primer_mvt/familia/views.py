from django.shortcuts import render
from familia.models import Familia
# from django.http import HttpResponse

# # Create your views here.
# def familia(request):
#     return render ( request, 'familia/tempate/inicio.html')

def home(request):

    familiares = Familia.objects.all()


    return render (request, "index.html",{"familiares":familiares})

