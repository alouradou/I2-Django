from django.conf import settings
from django.db import models
from django.utils import timezone



class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    def __str__(self):
        return self.id_equip


class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def actionLieux(self,lieu):
        if self.etat=='affame' and lieu.id_equip=='mangeoire' : #nourir
            self.etat = 'repus'
            return True
        elif self.etat == 'fatigue' and lieu.id_equip=='nid': #coucher
            self.etat = 'endormi'
            return True
        elif self.etat == 'endormi' and lieu.id_equip=='litiere': #reveiller
            self.etat = 'affame'
            return True
        elif self.etat == 'repus' and lieu.id_equip=='roue': #divertir
            self.etat = 'fatigue'
            return True
        else: return False
    def changeLieu(self,lieu):
        if lieu.disponibilite == 'libre' and self.actionLieux(lieu):
            self.lieu = lieu
            return self
        elif lieu.disponibilite == 'libre':
            return 'error_impossible'
        else:
            return 'error_not_empty'
    def __str__(self):
        return self.id_animal





class Billet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title