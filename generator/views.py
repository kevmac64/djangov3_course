from django.shortcuts import render
import random


# Create your views here.

def home(request):
    return render(request, 'generator/index.html', {
        'password':'dafjafoe'
    })
    # the dictionary is accessible on the page that we are sent too

def password(request):
    the_password = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*~<>?:;'))
    
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    for x in range(length):
        the_password += random.choice(chars)
    

    return render(request, 'generator/password.html', {
        'password': the_password,
    })

def about(request):
    return render(request, 'generator/about.html')