#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import pdb
import json


#Return a greeting.
def hola_mundo(request):

    now = datetime.now().strftime('''
        %b %dth, %Y - %H:%M hrs
        ''')

    return HttpResponse(f'''
        Hola, el tiempo actual del servidor es: {now}
        ''')

def numbers(request):
    #h
    #print(request)

    numbers = request.GET['x'].split(',')
    int_numb = []
    for n in numbers:
        int_numb.append(int(n))
    int_numb.sort()

    data = {
        'status' : 'ok',
        'numbers': int_numb,
        'message' : 'Integers Sorted Succsesfuly'
        }
    
    return HttpResponse(json.dumps(data, indent = 4), content_type = 'application/json')

def hi(request, age, name):
    if age > 18:
        return HttpResponse(json.dumps(f"Bienvenido {name}"))
    else:
        return HttpResponse(json.dumps(f'Acceso denegado, {name} no tienes edad suficiente para ingresar'))
    pass
