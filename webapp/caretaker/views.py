from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import user_passes_test

import datetime

from database.models import *

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def must_be_caretaker(user):
    return user.groups.filter(name="Opiekun").count()

@user_passes_test(must_be_caretaker, login_url='/login')
def seniors(request):
    seniors = Seniorzy.objects.all()
    seniors_rooms = {}
    for senior in seniors:
        room = "-"
        if senior.lozka != None:
            room = "Pokój nr {} - Piętro {}".format(senior.lozka.pokoje.numer, senior.lozka.pokoje.pietro)
        seniors_rooms[senior.id] = room

    context = {'seniors': seniors, 'seniors_rooms': seniors_rooms}
    return render(request, 'caretaker_seniors.html', context)

@user_passes_test(must_be_caretaker, login_url='/login')
def seniors_healthcard(request, id):
    senior = Seniorzy.objects.get(id=id)
    healthcard = senior.karty_zdrowia
    all_assigned_medicines = PrzyjmowaneLeki.objects.all().filter(karta_zdrowia=healthcard)
    assigned_medicines = [am for am in all_assigned_medicines if am.data_do >= datetime.date.today()]
    context = {'senior': senior, 'healthcard': healthcard, 'assigned_medicines': assigned_medicines}
    return render(request, 'caretaker_seniors_healthcard.html', context)

@user_passes_test(must_be_caretaker, login_url='/login')
def medicines(request):
    medicines = Leki.objects.all()
    context = {'medicines': medicines}
    return render(request, 'caretaker_medicines.html', context)

@user_passes_test(must_be_caretaker, login_url='/login')
def medicines_minus(request, id):
    medicine = Leki.objects.get(id=id)
    if medicine.ilosc_opakowan != 0:
        medicine.ilosc_opakowan -= 1
    medicine.save()
    return redirect(medicines)

@user_passes_test(must_be_caretaker, login_url='/login')
def medicines_plus(request, id):
    medicine = Leki.objects.get(id=id)
    medicine.ilosc_opakowan += 1
    medicine.save()
    return redirect(medicines)
