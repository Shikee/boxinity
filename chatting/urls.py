from django.urls import path
from . import views
urlpatterns = [
    path('api/box/', views.BoxListCreate.as_view() ),
]
