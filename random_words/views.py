
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime, localtime
from datetime import datetime
from django.utils.crypto import get_random_string


def random_page(request):
    counter = request.session.get('counter', 0)
    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    if counter == 10:
        context = {'randomword': 'Y0U H4V3 3XC33D3D TH3 L1M1T'}
    else:
        request.session['counter'] +=1
        context = {
        'randomword': get_random_string(length=14),
    }
    return render(request, "index.html", context)

def reset(request):
    counter = request.session['counter']= 0
    return redirect("/random")
    
def login(request):
    return render('login.html')

