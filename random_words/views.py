
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime, localtime
from datetime import datetime
from django.utils.crypto import get_random_string


def random_page(request):
    counter = ()
    if not counter:
        counter = 0
    context = {
        'randomword': get_random_string(length=14),
        'counter': counter
    }
    counter = counter + 1
    return render(request, "index.html", context)

def random(request):
    counter= 0
    context = {
        'randomword': get_random_string(length=14),
        'counter': counter
    }

def session_info(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100
