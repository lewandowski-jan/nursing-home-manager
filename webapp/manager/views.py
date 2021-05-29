from django.http import HttpResponse
from django.shortcuts import render

from database.models import *

def index(request):
    s = ''
    seniors = Seniorzy.objects.all()
    for senior in seniors:
        s += str(senior)
        s += '\n'
    return render(request, 'manager.html', {})