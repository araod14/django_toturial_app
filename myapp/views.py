from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task
from .form import CreateNewTask, CreateNewProject

createnewtask = CreateNewTask()
createnewproject = CreateNewProject()
# Create your views here.
def index(request):
    title = 'Django course!'
    return render(request,'index.html',
        {
        'title':title
        }
    )


def about(request):
    username = 'danel'
    return render(request, 'about.html', 
        {
        'username':username
        }
    )

def hello(request, username:str):
    print(username)
    return HttpResponse('<h2>Hello %s</h2>' %username)

def hello_id(request, id:int):
    return HttpResponse('<h2>Hello %s</h2>' %id)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', 
            {
            'projects':projects
            }
        )

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'task.html',
                  {
                    'tasks': tasks
                  }
        )

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', 
                      {
                        'form': createnewtask
                      }
            )
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            Project_id=2)
        return redirect('/tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html',
                      {
                        'form':createnewproject
                      }
                )
    else:
        Project.objects.create(name = request.POST['name'])
        return redirect('/projects')

def detail_project(request, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(Project_id=id)
    return render(request, 'detail_project.html',{
                        'project':project,
                        'tasks':tasks
                    }
                )