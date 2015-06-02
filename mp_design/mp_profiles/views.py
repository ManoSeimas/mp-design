from django.core.urlresolvers import reverse
from django.shortcuts import render


def index(request):
    context = {
        'items': [
            {'name': 'Frakcijos',
             'active': 'active',
             'url': reverse('fractions')},
            {'name': 'Parlamentarai',
             'active': False,
             'url': reverse('mps')},
        ]
    }
    return render(request, 'index.jade', context)


def fractions(request):
    context = {
        'items': [
            {'name': 'Frakcijos',
             'active': 'active',
             'url': reverse('fractions')},
            {'name': 'Parlamentarai',
             'active': False,
             'url': reverse('mps')},
        ]
    }
    return render(request, 'fractions.jade', context)


def fraction(request):
    return render(request, 'fraction.jade')


def mps(request):
    context = {
        'items': [
            {'name': 'Frakcijos',
             'active': False,
             'url': reverse('fractions')},
            {'name': 'Parlamentarai',
             'active': 'active',
             'url': reverse('mps')},
        ]
    }
    return render(request, 'mps.jade', context)


def parliamentarian(request):
    return render(request, 'parliamentarian.jade')
