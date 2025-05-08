from django.db import models
from django.contrib.auth.models import User

class Element(models.Model):
    numero = models.IntegerField(unique=True)
    symbole = models.CharField(max_length=5)
    nom = models.CharField(max_length=50)
    masse = models.FloatField()
    categorie = models.CharField(max_length=50)
    position_row = models.IntegerField()
    position_col = models.IntegerField()
    electronegativite = models.FloatField(null=True, blank=True)
    etat = models.CharField(max_length=10, choices=[('solide', 'Solide'), ('liquide', 'Liquide'), ('gaz', 'Gaz')], default='solide')
    masse_volumique = models.FloatField(null=True, blank=True)
    point_fusion = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.symbole})"

class ElementNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    element_id = models.IntegerField()
    note = models.TextField()

    def __str__(self):
        return f"Note for Element {self.element_id} by {self.user.username}"
