from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Animal, Billet, Equipement
from .forms import MoveForm

# Create your views here.


def post_list(request):
    billets = Billet.objects.order_by('published_date')
    return render(request, 'animalerie/post_list.html', {'billets': billets})

def animal_list(request):
    animals = Animal.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'animalerie/animal_list.html', {'animals': animals,'equipements': equipements})

def equipement_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'animalerie/animal_list.html', {'equipements': equipements})

def animal_detail(request,store_id):
    animal = Animal.objects.filter(id_animal=store_id)
    return render(request, 'animalerie/animal_list.html', {'animal': animal})

def post_new(request):
    form = MoveForm()
    return render(request, 'animalerie/post_edit.html', {'form': form})

def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    form=MoveForm(instance=animal)
    if form.is_valid():
        ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        ancien_lieu.disponibilite = "libre"
        print(ancien_lieu+'a ete libere !!')
        ancien_lieu.save()
        form.save()
        nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        nouveau_lieu.disponibilite = "occupe"
        nouveau_lieu.save()
        animal.lieu = nouveau_lieu
        animal.save()
        return redirect('animal_detail', id_animal=id_animal)
    else:
        lieu=animal.lieu
        form = MoveForm()
        return render(request,
                  'animalerie/animal_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form})