
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random
from datetime import date
from datetime import datetime

USERS = [
    {'nombre': 'Ruben','email': 'ruben@login.cl','clave': '123456'},
    {'nombre': 'Karen','email': 'karen@login.cl','clave': '141414'},
    {'nombre': 'Antonia','email': 'antonia@login.cl','clave': '232323'}
]

def ninja_login(request):
    if request.method == 'GET':
        request.session['name'] = 'error'
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
        return redirect("/ninja_values")
# FORMULARIO NINJA_RULES ESTA REDIRIGIENDO A REQUEST.POST.NINJA
def ninja_rules(request):
    ninja1min = request.POST['ninja1min']
    request.session['ninja1min'] = ninja1min
    
    ninja1max = request.POST['ninja1max']
    request.session['ninja1max'] = ninja1max
    
    ninja2min = request.POST['ninja2min']
    request.session['ninja2min'] = ninja2min
    
    ninja2max = request.POST['ninja2max']
    request.session['ninja2max'] = ninja2max
    
    ninja3min = request.POST['ninja3min']
    request.session['ninja3min'] = ninja3min
    
    ninja3max = request.POST['ninja3max']
    request.session['ninja3max'] = ninja3max
    
    ninja4min = request.POST['ninja4min']
    request.session['ninja4min'] = ninja4min
    
    ninja4max = request.POST['ninja4max']
    request.session['ninja4max'] = ninja4max
    
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
    ninja1min = request.session['ninja1min']
    ninja1max = request.session['ninja1max']
    ninja2min = request.session['ninja2min']
    ninja2max = request.session['ninja2max']
    ninja3min = request.session['ninja3min']
    ninja3max = request.session['ninja3max']
    ninja4min = request.session['ninja4min']
    ninja4max = request.session['ninja4max']
    
    # generar numero al azar
    form_ninja = request.POST['ninja']
    if form_ninja == 'kakashi':
        value = random.randint(int(ninja1min),int(ninja1max))
        date = datetime.now()
        if value < 0:
            dato = {'color': 'danger', 'message': f'You have lost {value * -1} by {form_ninja} at {date}'}
        elif value == 0:
            dato = {'color': 'dark', 'message': f'You have not been hit; your HP is not altered at {date}'}
        else:
            dato = {'color': 'success', 'message': f'You won {value} by {form_ninja} at {date}'}
    elif form_ninja == 'saske':
        value = random.randint(int(ninja2min),int(ninja2max))
        date = datetime.now()
        if value < 0:
            dato = {'color': 'danger', 'message': f'You have lost {value * -1} by {form_ninja} at {date}'}
        elif value == 0:
            dato = {'color': 'dark', 'message': f'You have not been hit; your HP is not altered at {date}'}
        else:
            dato = {'color': 'success', 'message': f'You won {value} by {form_ninja} at {date}'}
    elif form_ninja == 'naruto1':
        value = random.randint(int(ninja3min),int(ninja3max))
        date = datetime.now()
        if value < 0:
            dato = {'color': 'danger', 'message': f'You have lost {value * -1} by {form_ninja} at {date}'}
        elif value == 0:
            dato = {'color': 'dark', 'message': f'You have not been hit; your HP is not altered at {date}'}
        else:
            dato = {'color': 'success', 'message': f'You won {value} by {form_ninja} at {date}'}
    elif form_ninja == 'naruto2':
        value = random.randint(int(ninja4min),int(ninja4max))
        date = datetime.now()
        if value < 0:
            dato = {'color': 'danger', 'message': f'You have lost {value * -1} by Fake Jutsu Sexy at {date}'}
        elif value == 0:
            dato = {'color': 'dark', 'message': f'You have not been hit; your HP is not altered at {date}'}
        else:
            dato = {'color': 'success', 'message': f'You won {value} by Jutsu Sexy at {date}'}
    # sumarselos al HP
    request.session['hp'] += value
    request.session['messages'].append(dato)
    #redirigir
    return redirect("/ninja_gold")

def reborn(request):
    request.session['hp'] = 50
    request.session['messages'] = []
    return redirect("/ninja_gold")

def exit(request):
    request.session['hp'] = 50
    request.session['messages'] = []
    request.session['name'] = 'error'
    return redirect("/ninja_login")

def ninja_values(request):
    return render(request, "ninja_values.html")
