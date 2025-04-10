from django.db import models


class Element(models.Model):
    # File: Tableau_Periodique/models.py
    from django.db import models

    class Element(models.Model):
        numero = models.IntegerField()
        symbole = models.CharField(max_length=5)
        nom = models.CharField(max_length=50)
        masse = models.CharField(max_length=20)
        categorie = models.CharField(max_length=50)
        position_row = models.IntegerField()
        position_col = models.IntegerField()

        def __str__(self):
            return self.numero
            return self.symbole
            return self.nom
            return self.masse
            return self.categorie
            return self.position_row
            return self.position_col