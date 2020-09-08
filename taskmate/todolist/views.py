from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        # Fetch all the objects from DB
        all_tasks = TaskList.objects.all

        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def contact(request):
    context = {
        'contact_text': "Welcome to Contacts Page",
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': "Welcome from About Page",
    }
    return render(request, 'about.html', context)

def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def edit_task(request, task_id):
     if request.method == "POST":
         task = TaskList.objects.get(pk=task_id)
         form = TaskForm(request.POST or None, instance=task)
         if form.is_valid():
             form.save()
         messages.success(request, ("Task edited!"))
         return redirect('todolist')
    
     else:
        # Fetch all the objects from DB
        task_obj = TaskList.objects.get(pk=task_id)

        return render(request, 'edit.html', {'task_obj': task_obj})
