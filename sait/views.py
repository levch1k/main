from django.contrib.auth import logout
from django.db.transaction import commit
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm, CreateStatement
from django.contrib import messages, auth
import random

from .models import Statement


def index(request):
    if request.user.is_superuser:
        return redirect('admin_panel')
    if request.user.is_authenticated:
        statements = Statement.objects.filter(user=request.user)
        return render(request, 'sait/index.html', {'user': request.user, 'stat': statements})
    else:
        return render(request, 'sait/index.html')

def make_statement(request):
    if request.user.is_superuser:
        return redirect('admin_panel')
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateStatement(request.POST)
            if form.is_valid():
                stat = form.save(commit=False)
                stat.user = request.user
                stat.unique_id = random.randint(1488, 9999)
                stat.save()
                return redirect('index')
        else:
            form = CreateStatement()
            return render(request, 'sait/make_stat.html', {'user': request.user, 'form': form})
    else:
        return redirect('index')

def reg(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Вы успешно зарегистрированы!")
            return redirect('auth')
    else:
        form = UserRegistrationForm()
    return render(request, 'sait/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'sait/auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')

def admin_panel(request):
    if request.user.is_superuser:
        stat = Statement.objects.all()
        return render(request, 'sait/admin_panel.html', {'stat': stat, })
    else:
        return redirect('index')

def deny(request):
    if request.method == 'POST':
        statement_id = request.POST.get('id')
        statement = Statement.objects.get(id=statement_id)
        statement.status = 'Отклонено'  # установите ваш статус
        statement.save()
        return redirect('admin_panel')  # замените на вашу страницу
    return redirect('admin_panel') # Метод не разрешен

def accept(request):
    if request.method == 'POST':
        statement_id = request.POST.get('id')
        statement = Statement.objects.get(id=statement_id)
        statement.status = 'Принято'
        statement.save()
        return redirect('admin_panel')
    return redirect('admin_panel')