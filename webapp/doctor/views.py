from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import user_passes_test

import datetime

from database.models import *
from manager.forms import *

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
def edit_card(request):
    seniors = Seniorzy.objects.all()
    context = {'seniors': seniors}
    return render(request, 'doctor_seniors.html', context)

@user_passes_test(must_be_doctor, login_url='/login')
def edit_medicines(request):
    seniors = Seniorzy.objects.all()
    context = {'seniors': seniors}
    return render(request, 'doctor_seniors.html', context)