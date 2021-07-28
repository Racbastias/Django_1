
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime, localtime
from datetime import datetime


def func3(request, name):
    return HttpResponse(f'Hola hola hola {name}')

def func2(request):
    return HttpResponse("Holis")

def index(request):
    return HttpResponse('placeholder para luego mostrar una lista de todos los blogs')

def root(request):
    return redirect("blogs/")

def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f'placeholder para mostrar el blog numero: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder para editar el blog {number}')

def destroy(request, number):
    return redirect("/blogs")

def json(request):
    names = {
        "name": "Ruben",
        "edad": 33,
        "hobbies": ["Riding", "Reading", "Coding"]
    }
    return JsonResponse(names)

def home(request):
    data = {
        "moto" : "Honda CB500X 2016"
    }
    return render(request, 'home.html', data)

def times(request):
    information = {
        "day": strftime("%d", localtime()),
        "mes": strftime("%b", localtime()),
        "fullday": strftime("%A", localtime()),
        "date": strftime("%d %B %Y", localtime()),
        "localtime": strftime("%H:%M:%S", localtime())
    }
    return render(request, 'time.html', information)