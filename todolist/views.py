import datetime
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from todolist.forms import taskform, updateform
from todolist.models import tasklist
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

@login_required(login_url='/todolist/login/')

def add_task(request):
    if request.method == "POST":
        task_list = json.loads(request.POST['task_list'])
        new_task = tasklist(title=task_list["title"], description=task_list["description"], user=request.user)
        new_task.save()

        return HttpResponse(serializers.serialize("json", [new_task]), content_type="application/json")
    return HttpResponse()

def show_task(request):
    task_list = tasklist.objects.filter(user=request.user)
    context = {
        'task_list' : task_list,
        'username' : request.user.username,
    }
    return render(request, "todolist.html", context)

def show_json(request):
    task_list = tasklist.objects.filter(user= request.user)
    return HttpResponse(serializers.serialize("json",task_list), content_type="application/json")

def delete_task(request,task_id):
    queryset = tasklist.objects.get(id=task_id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('todolist:show_task')
    
    context = {
        'task':queryset
    }
    return render(request, 'delete_task.html', context)

def update_task(request,task_id):
	queryset = tasklist.objects.get(id=task_id)
	form = updateform(instance=queryset)
	if request.method == 'POST':
		form = updateform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('todolist:show_task')

	context = {
		'form':form
		}

	return render(request, 'update_task.html', context)

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
    response = HttpResponseRedirect(reverse("todolist:login"))
    response.delete_cookie('last_login')
    return redirect('todolist:login')