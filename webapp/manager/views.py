from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import user_passes_test

import datetime

from database.models import *
from manager.forms import NewSenior, NewCard, FormMedicine

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
def medicines_change_amount(request, id):
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

@user_passes_test(must_be_manager, login_url='/login')
def new_senior(request, cardid):
    formSenior = NewSenior()

    if request.POST:
        form = NewSenior(request.POST or None, request.FILES or None)

        if form.is_valid():
            senior = form.save(commit=False)
            senior.karty_zdrowia = KartyZdrowia.objects.get(id=cardid)
            senior.save()
        
        return redirect(seniors)
    
    return render(request, 'manager_new.html', context={'form': formSenior})

@user_passes_test(must_be_manager, login_url='/login')
def new_card(request):
    formCard = NewCard()

    if request.POST:
        form = NewCard(request.POST or None, request.FILES or None)

        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('/manager/seniors/new_senior/' + str(card.id))

    return render(request, 'manager_new.html', context={'form': formCard})

@user_passes_test(must_be_manager, login_url='/login')
def edit_medicine(request, id):
    medicine = Leki.objects.get(id = id)
    formMedicine = FormMedicine(instance=medicine)

    if request.POST:
        form = FormMedicine(request.POST or None, request.FILES or None, instance=medicine)

        if form.is_valid():
            form.save()
            return redirect(medicines)
    
    return render(request, 'manager_new.html', context={'form': formMedicine})