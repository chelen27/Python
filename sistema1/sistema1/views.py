from django.http import HttpResponse
from django.shortcuts import redirect


def saludo(request):
    x = 7
    y = 7
    mensaje = f"<h1>La suma es: {x+y} </h1>"
    return HttpResponse(mensaje)

def getGoogle(request):
    return redirect('https://www.google.com')
