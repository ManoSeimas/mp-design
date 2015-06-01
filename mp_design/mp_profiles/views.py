from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.jade')


def fractions(request):
    return render(request, 'fractions.jade')


def fraction(request):
    return render(request, 'fraction.jade')


def mps(request):
    return render(request, 'mps.jade')


def parliamentarian(request):
    return render(request, 'parliamentarian.jade')
