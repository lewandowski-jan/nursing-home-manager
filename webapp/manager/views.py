from django.http import HttpResponse
from django.shortcuts import render

from database.models import *

def workers(request):
    workers = Pracownicy.objects.all()
    context = {'workers': workers}
    return render(request, 'manager_workers.html', context)

def seniors(request):
    seniors = Seniorzy.objects.all()
    context = {'seniors': seniors}
    return render(request, 'manager_seniors.html', context)

def medicines(request):
    medicines = Leki.objects.all()
    context = {'medicines': medicines}
    return render(request, 'manager_medicines.html', context)