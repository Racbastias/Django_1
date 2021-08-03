
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random

USERS = [
    {'nombre': 'Ruben','email': 'ruben@login.cl','clave': '123456'},
    {'nombre': 'Karen','email': 'karen@login.cl','clave': '141414'},
    {'nombre': 'Antonia','email': 'antonia@login.cl','clave': '232323'}
]

def ninja_login(request):
    if request.method == 'GET':
        return render(request, "ninja_login.html")
    
    else:
        # primero recupero los input del formulario
        name_from_form = request.POST['nombre']
        email_from_form = request.POST['email']
        pass_from_form = request.POST['clave']
        
        # verifico si existe ESE usuario
        # usamos la función NEXT en vez de un for
        user = next((u for u in USERS if u['email'] == email_from_form), None)
        
        if user is None:
            request.session['name'] = 'error'
            return redirect("/ninja_login")
        
        # si llegamos acá. sabemos que si encontró un usuario con el mismo nombre
        
        if user['clave'] != pass_from_form:
            request.session['name'] = 'error'
            return redirect("/ninja_login")
        
        request.session['name'] = name_from_form
        request.session['pass'] = pass_from_form
        request.session['email'] = email_from_form
        request.session['messages'] = []
        request.session['hp'] = 50
        return redirect("/ninja_gold")
    
def ninja_gold(request):
    
    if 'hp' not in request.session:
        request.session['hp'] = 50
    if 'messages' not in request.session:
        request.session['messages'] = []
    context = {
        'hp' : request.session['hp']
    }
    return render(request, "ninja_gold.html", context)
    
def process_money(request):
    hp = request.session['hp']
    # generar numero al azar
    form_ninja = request.POST['ninja']
    if form_ninja == 'kakashi':
        value = random.randint(10,20)
        message = f'You won {value} by Copy Ninja'
    elif form_ninja == 'saske':
        value = random.randint(5,10)
        message = f'You have won {value} by Fire Ball'
    elif form_ninja == 'naruto1':
        value = random.randint(2,5)
        message = f'You have won {value} by Shadow Clones'
    elif form_ninja == 'naruto2':
        value = random.randint(-50,50)
        if value < 0:
            message = f'You have lost {value * -1} by Fake Jutsu Sexy'
        elif value == 0:
            message = f'You have not been hit; your HP is not altered'
        else:
            message = f'You have won {value} by Jutsu Sexy'
    # sumarselos al HP
    request.session['hp'] += value
    request.session['messages'].append(message)
    #redirigir
    return redirect("/ninja_gold")

def reborn(request):
    request.session['hp'] = 50
    request.session['messages'] = []
    return redirect("/ninja_gold")