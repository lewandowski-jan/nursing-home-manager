from django.shortcuts import render

from database.models import *

def seniors(request):
    seniors = Seniorzy.objects.all()
    context = {'seniors': seniors}
    return render(request, 'caretaker_seniors.html', context)

def medicines(request):
    medicines = Leki.objects.all()
    context = {'medicines': medicines}
    return render(request, 'caretaker_medicines.html', context)
