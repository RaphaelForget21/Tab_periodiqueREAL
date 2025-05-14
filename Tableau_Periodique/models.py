from django.db import models
from django.contrib.auth.models import User

class Element(models.Model):
    numero = models.IntegerField(unique=True,default=0)
    symbole = models.CharField(max_length=5)
    nom = models.CharField(max_length=50)
    masse = models.FloatField(default=0.0)
    categorie = models.CharField(max_length=50)
    position_row = models.IntegerField(default=0)
    position_col = models.IntegerField(default=0)
    electronegativite = models.FloatField(null=True, blank=True)
    etat = models.CharField(max_length=10, choices=[('solide', 'Solide'), ('liquide', 'Liquide'), ('gaz', 'Gaz')], default='solide')
    masse_volumique = models.FloatField(null=True, blank=True)
    point_fusion = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} ({self.symbole})"

class ElementNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    note = models.TextField()

    class Meta:
        unique_together = ('user', 'element')



    def __str__(self):
        return f"Note for Element {self.element} by {self.user.username}"
