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
            return ''
        elif self.etat == 'fatigue' and lieu.id_equip=='nid': #coucher
            self.etat = 'endormi'
            return ''
        elif self.etat == 'endormi' and lieu.id_equip=='litiere': #reveiller
            self.etat = 'affame'
            return ''
        elif self.etat == 'repus' and lieu.id_equip=='roue': #divertir
            self.etat = 'fatigue'
            return ''
        else:
            if lieu.id_equip=='mangeoire':
                return "je n'ai pas faim"
            elif lieu.id_equip=='nid':
                return "je n'ai pas sommeil"
            elif lieu.id_equip=='litiere':
                return "je ne dors pas"
            elif lieu.id_equip=='roue':
                return "je n'ai pas le coeur à m'amuser..."
            else : return '...erreur'

    def changeLieu(self,lieu):
        reason = self.actionLieux(lieu)
        if lieu.disponibilite == 'libre' and not reason:
            self.lieu = lieu
            return self
        elif lieu.disponibilite == 'libre':
            return 'error_impossible:'+reason
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