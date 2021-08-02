
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

USERS = [
    {'nombre': 'Ruben','email': 'ruben@login.cl','clave': '123456'},
    {'nombre': 'Karen','email': 'karen@login.cl','clave': '141414'},
    {'nombre': 'Antonia','email': 'antonia@login.cl','clave': '232323'}
]

def random_page(request):
    counter = request.session.get('counter', 0)
    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    if counter == 10:
        context = {'randomword': ''}
    else:
        request.session['counter'] +=1
        context = {
        'randomword': get_random_string(length=14),
    }
    return render(request, "index.html", context)

def reset(request):
    request.session['counter']= 0
    return redirect("/random")
    

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
        return redirect("/ninja_gold")
    
def ninja_gold(request):
    request.session['counter']= 0
    return render(request, "ninja_gold.html")
    
def process_money(request):
    request.session['counter']= 0
    return redirect("/ninja_gold")
    