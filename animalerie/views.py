from django.shortcuts import render
from django.utils import timezone
from .models import Billet


# Create your views here.


def post_list(request):
    billets = Billet.objects.order_by('published_date')
    return render(request, 'animalerie/post_list.html', {'billets': billets})