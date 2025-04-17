from django.db import models


class Element(models.Model):
    numero = models.IntegerField()
    symbole = models.CharField(max_length=5)
    nom = models.CharField(max_length=50)
    masse = models.CharField(max_length=20)
    categorie = models.CharField(max_length=50)
    position_row = models.IntegerField()
    position_col = models.IntegerField()
    atomic_radius = models.CharField(max_length=10, default="x")
    electronegativity = models.CharField(max_length=10, default="x")
    melting_point = models.CharField(max_length=10, default="x")

    def __str__(self):
        return f"{self.numero} - {self.symbole} - {self.nom} - {self.masse} - {self.categorie} - Row: {self.position_row} - Col: {self.position_col} - Radius: {self.atomic_radius} - EN: {self.electronegativity} - MP: {self.melting_point}"

