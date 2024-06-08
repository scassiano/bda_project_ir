from django.shortcuts import render
from .models import egresados_collection
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<iframe title="DefinitivoDashboard" width="1080" height="720" src="https://app.powerbi.com/view?r=eyJrIjoiYzFkZTg2NDEtNWQ4Mi00YmY0LWFiMjEtM2FiYTk0ZTQ0OTAyIiwidCI6IjU3N2ZjMWQ4LTA5MjItNDU4ZS04N2JmLWVjNGY0NTVlYjYwMCIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>')


def get_all_egresados(request):
    egresados = egresados_collection.find({ "$text": { "$search": "educación en la infancia","$language":"es", "$diacriticSensitive":True} }, {"score": { "$meta": "textScore" } }).sort( { "score": { "$meta": "textScore" } })
    return HttpResponse(egresados)