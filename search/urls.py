from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("egresado/<str:id>",views.get_egresado)
]