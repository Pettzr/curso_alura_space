from django.shortcuts import render
# from django.http import HttpResponse # nao será preciso, pois importamos o código

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
