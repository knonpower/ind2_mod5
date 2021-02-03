from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'base.html')

def imagenes(request):
    return render(request, 'app_miproyecto/index.html')

def index2(request):
    diccionario = {"one": "uno", 
                "two": "dos",
                "three":"tres", 
                "four": "cuatro", 
                "five":" cinco"
                }
    context = {"diccionario": diccionario}
    return render(request, 'app_miproyecto/index2.html', context)
