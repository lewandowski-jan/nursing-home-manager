from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import user_passes_test

import datetime

from database.models import *

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def must_be_manager(user):
    return user.groups.filter(name="Manager").count()

@user_passes_test(must_be_manager, login_url='/login')
def workers(request):
    workers = Pracownicy.objects.all()
    context = {'workers': workers}
    return render(request, 'manager_workers.html', context)

@user_passes_test(must_be_manager, login_url='/login')
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

@user_passes_test(must_be_manager, login_url='/login')
def workers(request):
    workers = Pracownicy.objects.all()
    context = {'workers': workers}
    return render(request, 'manager_workers.html', context)

@user_passes_test(must_be_manager, login_url='/login')
def medicines(request):
    medicines = Leki.objects.all()
    context = {'medicines': medicines}
    return render(request, 'manager_medicines.html', context)

@user_passes_test(must_be_manager, login_url='/login')
def medicines_add(request, id):
    if request.POST:
        medicine = Leki.objects.get(id=id)
        input = request.POST.get('new_amount')
        try:
            input = int(input)
        except ValueError:
            return redirect(medicines)

        medicine.ilosc_opakowan = input
        medicine.save()
    return redirect(medicines)