from django.db import models
from django.contrib.auth.models import User


class Element(models.Model):
    numero = models.IntegerField(null=True, blank=True)
    symbole = models.CharField(max_length=5)
    nom = models.CharField(max_length=100)
    masse = models.FloatField(null=True, blank=True)
    categorie = models.CharField(max_length=50)
    position_row = models.IntegerField(null=True, blank=True)
    position_col = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return f"{self.numero} - {self.symbole} - {self.nom} - {self.masse} - {self.categorie} - Row: {self.position_row} - Col: {self.position_col}"


class ElementNote(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f"Note for {self.element.nom} by {self.user.username}"