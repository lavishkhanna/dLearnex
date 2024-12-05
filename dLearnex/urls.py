"""
URL configuration for dLearnex project.

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
from turtle import home
from django.contrib import admin
from django.urls import path
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),


    # POST
    path('register/', register_user, name='register'),
    path('', home_view, name='home'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('protected/', protected_view, name='protected'),
    path('pref/', take_prefs, name='take_prefs'),
    path('take_top/', take_top, name='take_top'),
    path('course/<str:course_name>/', course_view, name='course_details'),

    # GET
    path('user/', get_user_data, name='get_user_data'),
    path('show_pref/', show_pref, name='show_pref'),
    path('recommendations/', get_recommendations, name='get_recommendations'),
]