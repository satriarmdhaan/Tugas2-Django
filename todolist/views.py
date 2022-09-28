import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import taskform
from todolist.models import tasklist
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login/')
def show_task(request):
    task_list = tasklist.objects.filter(user= request.user)
    context = {
        'task_list' : task_list,
        'username' : request.user.username,
    }
    return render(request, "todolist.html", context)

def delete_task(request, id):
    task_list = tasklist.objects.filter(id=id)
    task = task_list[0]
    task.delete()
    return redirect('todolist:show_task')

def update_task(request, id):
    task_list = tasklist.objects.filter(id=id)
    task = task_list[0]
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_task')

def create_task(request):
    form = taskform()
    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('todolist:show_task')
        else:
            form = taskform()
    context = {'form': form}
    return render(request, 'create-task.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_task"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:show_task"))
    response.delete_cookie('last_login')
    return response