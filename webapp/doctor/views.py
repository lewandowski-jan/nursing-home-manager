from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

import datetime

from database.models import *
from doctor.forms import FormHealthCard, FormAssignedMedicine

def must_be_doctor(user):
    return user.groups.filter(name="Lekarz").count()

@user_passes_test(must_be_doctor, login_url='/login')
def seniors(request):
    seniors = Seniorzy.objects.all()
    context = {'seniors': seniors}
    return render(request, 'doctor_seniors.html', context)

@user_passes_test(must_be_doctor, login_url='/login')
def senior_card(request, id):
    senior = Seniorzy.objects.get(id=id)
    healthcard = senior.karty_zdrowia
    all_assigned_medicines = PrzyjmowaneLeki.objects.all().filter(karta_zdrowia=healthcard)
    assigned_medicines = [am for am in all_assigned_medicines if am.data_do >= datetime.date.today()]
    context = {'senior': senior, 'healthcard': healthcard, 'assigned_medicines': assigned_medicines}
    return render(request, 'doctor_seniors_healthcard.html', context)

@user_passes_test(must_be_doctor, login_url='/login')
def edit_card(request, id):
    senior = Seniorzy.objects.get(id=id)
    healthcard = senior.karty_zdrowia
    formHealtCard = FormHealthCard(instance=healthcard)

    if request.POST:
        form = FormHealthCard(request.POST or None, request.FILES or None, instance=healthcard)

        if form.is_valid():
            form.save()
            return redirect(seniors)
    
    return render(request, 'doctor_form.html', context={'form': formHealtCard, "senior": senior})

@user_passes_test(must_be_doctor, login_url='/login')
def assigned_medicines(request, id):
    senior = Seniorzy.objects.get(id=id)
    healthcard = senior.karty_zdrowia
    assigned_medicines = PrzyjmowaneLeki.objects.all().filter(karta_zdrowia=healthcard)
    context = {'senior': senior, 'assigned_medicines': assigned_medicines}
    return render(request, 'doctor_medicines.html', context)

@user_passes_test(must_be_doctor, login_url='/login')
def assigned_medicine_remove(request, id):
    assigned_medicine = PrzyjmowaneLeki.objects.get(id=id)
    healthcard = assigned_medicine.karta_zdrowia
    senior = Seniorzy.objects.get(karty_zdrowia=healthcard)
    if assigned_medicine != None:
        assigned_medicine.delete()
    return redirect(assigned_medicines, senior.id)

@user_passes_test(must_be_doctor, login_url='/login')
def assigned_medicine_add(request, id):
    senior = Seniorzy.objects.get(id=id)
    healthcard = senior.karty_zdrowia
    formAssignedMedicine = FormAssignedMedicine()

    if request.POST:
        form = FormAssignedMedicine(request.POST or None, request.FILES or None)

        if form.is_valid():
            print('hello')
            assignedmedicine = form.save(commit=False)
            assignedmedicine.karta_zdrowia = healthcard
            assignedmedicine.save()
            return redirect(assigned_medicines, senior.id)

    return render(request, 'doctor_form.html', context={'form': formAssignedMedicine, "senior": senior})
