"""
URL configuration for recipe_finder project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from userapp import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name = "home"),
    path('otp/', views.otp, name = "otp"),
    path('login/', views.login_page_view, name = "login"),
    path('recipes/', views.recipes_page_view, name = "recipes"),
    path('veg-recipes/', views.veg_recipes_page_view, name = "veg-recipes"),
    path('nonveg-recipes/', views.nonveg_recipes_page_view, name = "nonveg-recipes"),
    path('samosa/', views.samosa, name = "samosa"),
    path('chillipaneer/', views.chillipaneer, name = "chillipaneer"),
    path('dabeli/', views.dabeli, name = "dabeli"),
    path('vegfriedrice/', views.vegfriedrice, name = "vegfriedrice"),
    path('phulka/', views.phulka, name = "phulka"),
    path('vegbiryani/', views.vegbiryani, name = "vegbiryani"),
    path('gulabjamun/', views.gulabjamun, name = "gulabjamun"),
    path('jalebi/', views.jalebi, name = "jalebi"),
    path('kheer/', views.kheer, name = "kheer"),
    path('chickenspringrolls/', views.chickenspringrolls, name = "chickenspringrolls"),
    path('chilliprawns/', views.chilliprawns, name = "chilliprawns"),
    path('muttonkeemasamosa/', views.muttonkeemasamosa, name = "muttonkeemasamosa"),
    path('butterchicken/', views.butterchicken, name = "butterchicken"),
    path('chickenbiryani/', views.chickenbiryani, name = "chickenbiryani"),
    path('muttonbiryani/', views.muttonbiryani, name = "muttonbiryani"),
]