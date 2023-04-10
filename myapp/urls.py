from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('hello/<str:username>', views.hello),
    path('hello_id/<int:id>', views.hello_id),
    path('projects', views.projects),
    path('create_task', views.create_task),
    path('create_project', views.create_project),
    path('detail_project/<int:id>', views.detail_project),
    path('tasks', views.tasks)
]
