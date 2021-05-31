from django.shortcuts import render, redirect
from django.template.defaulttags import register

import datetime

from database.models import *

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def workers(request):
    workers = Pracownicy.objects.all()
    context = {'workers': workers}
    return render(request, 'manager_workers.html', context)

def seniors(request):
    seniors = Seniorzy.objects.all()
    seniors_rooms = {}
    for senior in seniors:
        room = "-"
        if senior.lozka != None:
            room = "Pokój nr {} - Piętro {}".format(senior.lozka.pokoje.numer, senior.lozka.pokoje.pietro)
        seniors_rooms[senior.id] = room

    context = {'seniors': seniors, 'seniors_rooms': seniors_rooms}
    return render(request, 'manager_seniors.html', context)


def workers(request):
    workers = Pracownicy.objects.all()
    context = {'workers': workers}
    return render(request, 'manager_workers.html', context)

def medicines(request):
    medicines = Leki.objects.all()
    context = {'medicines': medicines}
    return render(request, 'manager_medicines.html', context)

def medicines_add(request, id):
    medicine = Leki.objects.get(id=id)
    input = (request.GET.get('amount'))

    try:
        input = int(input)
    except ValueError:
        return redirect(medicines)

    medicine.ilosc_opakowan = input
    medicine.save()
    return redirect(medicines)