from django.shortcuts import render
from .models import egresados_collection
from django.http import HttpResponse

# Create your views here.
def index(request):
    query = request.GET.get('q', '')
    egresados = egresados_collection.find(
        { 
            "$text": { 
                "$search": query,
                "$language":"es",
                "$diacriticSensitive":True
            }
        },
        {
            "score":{
                "$meta": "textScore"
            }
        }).sort(
            { "score": {
                "$meta": "textScore"
                }
            })
    return render(request, "search.html",{"lista":egresados})

def get_egresado(request, id):
    egresado = egresados_collection.find_one({"personal.identificacion":int(id)})
    pokemon = str(int(id) % 1025).zfill(3)
    return render(request, "egresado.html",{"egresado":egresado, "pokemon": pokemon})