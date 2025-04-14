from django.db import models

# Create your models here.
class Events(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    organisateurs = models.ForeignKey('Organisateurs', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom


    
class Organisateurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    sexe = models.CharField(max_length=10)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.nom
    


class Invites(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    sexe = models.CharField(max_length=10)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.nom
    

class Tickets(models.Model): 
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    invites = models.ForeignKey(Invites, on_delete=models.CASCADE)
    usersemail = models.EmailField()
    eventsname = models.ForeignKey(Events, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.invites} - {self.eventsname}"
    