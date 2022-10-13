from todolist.views import add_task, delete_task, logout_user, login_user, register , show_json, show_task, create_task, update_task, delete_task
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update-task/<int:task_id>', update_task, name='update_task'),
    path('delete-task/<int:task_id>', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task')
]