"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name="homePage"),
    path('registerPage/',registerPage, name="registerPage"),
    path('loginPage/',loginPage, name="loginPage"),
    path('logoutPage/',logoutPage, name="logoutPage"),
    path('profilePage/',profilePage, name="profilePage"),
    path('createdJob/',createdJob, name="createdJob"),
    path('addJob/',addJob, name="addJob"),
    path('deleteJob/<int:job_id>',deleteJob, name="deleteJob"),
    path('editJob/<int:job_id>',editJob, name="editJob"),
    path('viewJob/<int:job_id>',viewJob, name="viewJob"),
    path('applyJob/<int:job_id>',applyJob, name="applyJob"),
    path('searchJob/',searchJob, name="searchJob"),
    path('skillMatchingPage/',skillMatchingPage, name="skillMatchingPage"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
