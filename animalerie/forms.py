from django import forms
 
from .models import Animal, Equipement
 
class MoveForm(forms.ModelForm):
 
    class Meta:
        model = Animal
        fields = ('lieu',)

class submitPhoto(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('photo',)


class freeSpace(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = ('disponibilite',)