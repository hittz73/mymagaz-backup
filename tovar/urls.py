from django.urls import path
from . import views

urlpatterns = [
    path('', views.tovar_home, name='tovar_home')
]
