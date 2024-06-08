from django.shortcuts import render
from .models import egresados_collection
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "search.html")


def get_all_egresados(request):
    egresados = egresados_collection.find({ "$text": { "$search": "educación en la infancia","$language":"es", "$diacriticSensitive":True} }, {"score": { "$meta": "textScore" } }).sort( { "score": { "$meta": "textScore" } })
    return HttpResponse(egresados)