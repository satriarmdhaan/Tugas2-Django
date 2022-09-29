## Link HEROKUAPP

Link: [Link](https://django-tugas2.herokuapp.com/todolist/login/?next=/todolist/)

## Kegunaan `{% csrf_token %}` pada elemen `<form>` dan apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`
CSRF token atau _Cross-Site Request Forgery_ token memiliki fungsi sebagai autentikasi untuk `HTTP Request` yang datang dari aplikasi yang telah dibuat dan untuk menangkal serangan. Hal yang terjadi apabila tidak ada `{% csrf_token %}` pada elemen `<form>` adalah akun tidak dapat di autentikasi dan `HTTP Request` tidak dapat diverifikasi sehingga `HTTP Request` akan dibatalkan.

## Membuat elemen `<form>` secara manual (tanpa generator seperti `{{form.as_table}}`)
Elemen `<form>` dapat dibuat secara manual tanpa generator seperti `{{form.as_table}}` dengan menggunakan wrapper. Untuk implementasinya, pertama tentukanlah atribut `method` dan `action` dari `<form>` terlebih dahulu. Atribut `method` berguna untuk menerapkan `HTTP method` yang akan digunakan, contohnya `POST`. Sedangkan atribut `action` berfungsi sebagai tujuan pengiriman data dari atribut `method`. Setelah keduanya diisi, elemen-elemen yang ingin ditampilkan bisa langsung diaplikasikan dengan memasukkannya ke dalam wrapper dengan mengisi atribut `input type` yang berfungsi untuk menentukan tipe data yang akan ditampilkan serta `name`, yaitu key dari `value` dan terakhir `value`, yaitu data itu sendiri. Selanjutnya, buatlah sebuah _button_ untuk submisi dari form yang telah dibuat.

## Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada _template_ HTML.
Data-data yang telah di submisi melalui HTML form akan masuk kedalam server melalui `HTTP Request` sesuai dengan atribut `method` dan atribut `action` yang ada pada `<form>`. Setelah melakukan `HTTP Request`, permintaan data akan disalurkan melalui atribut `action` dengan menyesuaikan value url dari atribut `action` dengan list `urlpatterns` yang ada pada `urls.py`. Setelah itu, data akan diproses melalui `method` atau _function_ yang sesuai pada `views.py` dan lalu di _render_ menuju HTML.

## Cara implementasi
1. Membuat `django-app` bernama `todolist` dengan perintah `python manage.py startapp todolist`.
2. Buka `settings.py` pada folder `project_django` dan tambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan `django-app` yang sudah dibuat.
```
INSTALLED_APPS = [
    ...,
    'todolist',
]
```
3. Ubahlah literal dari `LANGUAGE_CODE` yang ada pada `settings.py` di folder `project_django` menjadi `'id'` dan gantilah literal dari `TIME_ZONE` menjadi `'Asia/Jakarta'`.

4. Buka `urls.py` pada folder `project_django` dan tambahkan path `todolist` seperti, sebagai berikut.
```
urlpatterns = [
    ...,
    path('todolist/', include('todolist.urls)),
]
```

5. Buka file `models.py` yang ada pada folder `todolist` dan tambahkan potongan kode berikut.
```
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class tasklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=255)
    description = models.CharField(max_length= 255)
    is_finished = models.BooleanField(default=False)
```
6. Buka file `views.py` dan tambahkan kode berikut.
```
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
    task_list.delete()
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
```
7. Buatlah file baru bernama `forms.py` dalam folder `todolist` dengan kode sebagai berikut.
```
from django.forms import ModelForm
from todolist.models import tasklist

class taskform(ModelForm):
    class Meta:
        model = tasklist
        fields = [
            'title',
            'description'
        ]
```
8. Buatlah file baru bernama `urls.py` dalam folder `todolist` dengan kode sebagai berikut.
```
from todolist.views import delete_task, logout_user, login_user, register, show_task, create_task, update_task, delete_task
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update-task/<int:id>', update_task, name='update_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]
```
9. Buatlah folder baru bernama `templates` dalam folder `todolist` dan buatlah file `todolist.html`, `register.html`, `login.html` dan `create-task.html`.

10. Dalam file `todolist.html` yang ada pada folder `templates`,tambahkanlah kode sebagai berikut.
```
{% extends 'base.html' %}

{% block content %}

<h1>Tugas 4 PBP/PBD</h1>
<h3>Name: {{username}} </h3>

<style>
table, th, tr {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
<table>
  <tr>
  <th>Status</th>
  <th>Date</th>
  <th>Title</th>
  <th>Description</th>
  <th>Update Task</th>
  <th>Delete Task</th>
  </tr>

  {% for todolist in task_list %}
  
  <tr>
    {% if todolist.is_finished %}
      <th>Sudah</th>
    {% else %}
      <th>Belum</th>
    {% endif %}
    <th>{{todolist.date}}</th>
    <th>{{todolist.title}}</th>
    <th>{{todolist.description}}</th>
    <th>
      <button>
        <a href="{% url 'todolist:update_task' todolist.id %}">Update</a>
      </button>
    </th>
    <th>
      <button>
        <a href="{% url 'todolist:delete_task' todolist.id %}">Delete</a>
      </button>
    </th>
  </tr>
  {% endfor %}
</table>

<button>
    <a href="{% url 'todolist:create_task' %}">Tambah Task Baru</a>
</button>

<button>
    <a href="{% url 'todolist:logout' %}">Logout</a>
</button>
{% endblock content %}
```
11. Dalam file `register.html` yang ada pada folder `templates`, tambahkanlah kode sebagai berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
12. Pada file `login.html` yang ada pada folder `templates`, tambahkanlah kode sebagai berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```
13. Pada file `create-task.html` yang ada pada folder `templates`, tambahkanlah kode sebagai berikut.
```
{% extends 'base.html' %}


{% block content %}  
<title>Tambah Task Baru</title>

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>
</div>  

{% endblock content %}
```
14. Jalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam _database_ Django lokal.
15. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam _database_ Django lokal.
16. Melakukan `add`, `commit`, dan `push` ke dalam github.