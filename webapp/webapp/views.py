from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return redirect('/login')

def login_user(request):
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            groups = user.groups.all()
            if str(groups[0]) == "Opiekun":
                return redirect('/caretaker')
            elif str(groups[0]) == "Manager":
                return redirect('/manager')
            elif str(groups[0]) == "Lekarz":
                return redirect('/doctor')
        else: 
            return render(request, 'failed_login.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login')

def view_404(request, exception=None):
    return redirect('/login')