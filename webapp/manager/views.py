from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import user_passes_test

import datetime

from database.models import *
from manager.forms import NewSenior, NewCard, FormMedicine, FormWorker, FormSenior, NewPostal, NewAddress, NewWorker, NewMedicine

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

@user_passes_test(must_be_manager, login_url='/login')
def edit_worker(request, id):
    worker = Pracownicy.objects.get(id = id)
    formWorker = FormWorker(instance=worker)

    if request.POST:
        form = FormWorker(request.POST or None, request.FILES or None, instance=worker)

        if form.is_valid():
            form.save()
            return redirect(workers)
    
    return render(request, 'manager_new.html', context={'form': formWorker})

@user_passes_test(must_be_manager, login_url='/login')
def edit_senior(request, id):
    senior = Seniorzy.objects.get(id = id)
    formSenior = FormSenior(instance=senior)

    if request.POST:
        form = FormSenior(request.POST or None, request.FILES or None, instance=senior)

        if form.is_valid():
            form.save()
            return redirect(seniors)
    
    return render(request, 'manager_new.html', context={'form': formSenior})


@user_passes_test(must_be_manager, login_url='/login')
def new_postal(request):
    formPostal = NewPostal()

    if request.POST:
        form = NewPostal(request.POST or None, request.FILES or None)

        if form.is_valid():
            postal = form.save(commit=False)
            postal.save()
            return redirect('/manager/workers/new_address/' + str(postal.id))

    return render(request, 'manager_new.html', context={'form': formPostal})

@user_passes_test(must_be_manager, login_url='/login')
def new_address(request, postalid):
    formAddress = NewAddress()

    if request.POST:
        form = NewAddress(request.POST or None, request.FILES or None)

        if form.is_valid():
            address = form.save(commit=False)
            address.poczty = Poczty.objects.get(id=postalid)
            address.save()
        
            return redirect('/manager/workers/new_worker/' + str(address.id))
    
    return render(request, 'manager_new.html', context={'form': formAddress})


@user_passes_test(must_be_manager, login_url='/login')
def new_worker(request, addressid):
    formWorker = NewWorker()

    if request.POST:
        form = NewWorker(request.POST or None, request.FILES or None)

        if form.is_valid():
            worker = form.save(commit=False)
            worker.adresy = Adresy.objects.get(id=addressid)
            worker.save()
        
        return redirect(workers)
    
    return render(request, 'manager_new.html', context={'form': formWorker})


@user_passes_test(must_be_manager, login_url='/login')
def new_medicine(request):
    formMedicine = NewMedicine()

    if request.POST:
        form = NewMedicine(request.POST or None, request.FILES or None)

        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.save()
        
        return redirect(medicines)
    
    return render(request, 'manager_new.html', context={'form': formMedicine})

