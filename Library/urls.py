"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Book.views import *
from subscribe.views import subscribe_email
# from Book.views.first_views import func1
# from Book.views.second_views import func2
# OR
from Book import views     # when entries done in init.py under views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.homepage ,name="home"),
    path('show_books_data/',views.get_book_data ,name="show_books"),
    path('delete-book/<int:id>/',views.delete_book,name="delete"),
    path('soft-delete-book/<int:id>/',views.soft_delete_book,name="soft_delete"),
    path('update-book/<int:id>/',views.update_book,name="update"),
    path('active-books/',views.active_books,name="active_books"),
    path('inactive-books/',views.inactive_books,name="inactive_books"),
    path('restore-book/<int:id>/',views.restore_book,name="restore_book"),
    # Email
    path('email-home/',subscribe_email,name='subscribe_email'),

    path('func1/',func1,name='func1'),       # when entries not done in init.py under views
    #OR
    path('func1/',views.func1,name='func1'),
    path('func2/',views.func2,name='func2'), # when entries done in init.py under views
]

