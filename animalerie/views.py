from django.shortcuts import render
from django.utils import timezone
from .models import Animal, Billet, Equipement


# Create your views here.


def post_list(request):
    billets = Billet.objects.order_by('published_date')
    return render(request, 'animalerie/post_list.html', {'billets': billets})

def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animals': animals})

def equipement_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animals': equipements})

def animal_detail(request,store_id):
    animal = Animal.objects.filter(id_animal=store_id)
    return render(request, 'animalerie/animal_list.html', {'animal': animal})
