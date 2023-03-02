from django.db import models

class Reservation(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=200)
    date = models.DateField()
    heure = models.TimeField()
    nb_personnes = models.IntegerField()
    message = models.TextField()

class User(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


# Create your models here.
