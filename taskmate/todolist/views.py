from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:
        # Fetch all the objects from DB
        all_tasks = TaskList.objects.all

        return render(request, 'todolist.html', {'all_tasks': all_tasks})
        # context = {
        #     'welcome_text': "Welcome to Todolist",
        # }
        # return render(request, 'todolist.html', context)


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
