from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("showall/",views.get_all_egresados)
]