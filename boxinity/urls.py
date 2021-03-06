"""boxinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework import routers
from chatting import views
from django.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatting.urls')),
    # path('users/', include('users.urls')),
    path('api/users/', include('rest_auth.urls')),

    # path('api/box/', views.BoxListCreate.as_view() ),
    # path('', views.UserListCreate.as_view()),

    # path('api/users/create', views.UserListView.as_view(), name='account-create'),
    # path('api/users/login', views.UserLogin.as_view(), name='account-login'),

]
