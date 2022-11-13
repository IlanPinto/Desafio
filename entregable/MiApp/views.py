from django.shortcuts import render
from MiApp.models import Familiares

# Create your views here.
def mostrar_familiares(request):
    familiar_1 = Familiares(nombre = "Mario", edad = 50, nacimiento = "1972-06-15")
    familiar_2 = Familiares(nombre = "Tatiana", edad = 19, nacimiento = "2002-12-17")
    familiar_3 = Familiares(nombre = "Federico", edad = 24, nacimiento = "1998-09-24")
    return render(request, 'MiApp/familiares.html', {'familiares':[familiar_1,familiar_2,familiar_3]})

def mostrar_index(request):
    return render(request,'MiApp/index.html')
