from django.http import HttpResponse
from django.shortcuts import render

from database.models import *

def manager_workers(request):
    
    workers = Pracownicy.objects.all()
    context = {'workers': workers}

    return render(request, 'manager_workers.html', context)