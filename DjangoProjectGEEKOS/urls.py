"""
URL configuration for DjangoProjectGEEKOS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Tableau_Periodique import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/elements/', views.get_elements_json, name='get_elements_json'),
    path('periodic_table/', views.periodic_table_view, name='periodic_table'),  # Example for the periodic table page
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('save-note/', views.save_note_view, name='save_note'),
    path('get-note/', views.get_note_view, name='get_note'),

]
