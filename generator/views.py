from django.shortcuts import render
from django.http import HttpResponse

import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    lenght = int(request.GET.get('lenght'))

    protection_levels = ['secondary', 'danger', 'warning', 'success']
    texts = [
        'too simple',
        'pretty simple. Maybe you want to improve it?',
        'nice, but maybe you want to make it even stronger',
        'great!',
            ]
    protection_level = 0

    if request.GET.get('uppercase'):
        protection_level += 1
        symbols = string.ascii_letters
    else:
        symbols = string.ascii_lowercase
        if lenght >= 12:
            protection_level += 1

    if request.GET.get('numbers'):
        symbols += string.digits
        protection_level += 1
    if request.GET.get('special'):
        symbols += '!@#$%^&*()'
        protection_level += 1

    _password = ''.join([random.choice(symbols) for _ in range(lenght)])

    return render(request,
                  'generator/password.html',
                  {'password': _password, 'password_protection': protection_levels[protection_level], 'text': texts[protection_level]}
                  )


def about(request):
    return render(request, 'generator/about.html')
