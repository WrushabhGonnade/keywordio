"""My_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminshow/',views.showbooks),
    path('delete/<int:id>', views.delete),
    path('addbook/',views.add_book,name='addbook'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('signup/',views.UserRegistration, name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('',views.home),
    path('studentview/',views.studentview),
    path('logout/',auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('select/',views.select,name='select'),
]
