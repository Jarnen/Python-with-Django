from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    context = {
        'welcome_text': "Welcome to Todolist",
    }
    return render(request, 'todolist.html', context)


def contact(request):
    context = {
        'welcome_text': "Welcome to Contacts Page",
    }
    return render(request, 'contacts.html', context)


def about(request):
    context = {
        'welcome_text': "Welcome from About Page",
    }
    return render(request, 'about.html', context)
