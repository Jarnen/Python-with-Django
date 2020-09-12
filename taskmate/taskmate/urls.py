
from django.contrib import admin
from django.urls import path, include
from todolist import views as todolist_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', todolist_views.index, name='index'),
    path('accounts/', include('users.urls')),
    path('todolist/', include('todolist.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about', todolist_views.about, name='about'),
]
