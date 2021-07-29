
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime, localtime
from datetime import datetime
#from djanjo.utils import get_random_string


def random_page(request):
    return render(request, "index.html")

#def random(request):
#    if 'counter' no existe:
#    'counter'++
#        'counter' = 0
#    context = {'randomword': get_random_string(length=14),
#        'counter': 'counter'
