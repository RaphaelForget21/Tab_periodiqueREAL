from django.core.management.base import BaseCommand
from Tableau_Periodique.models import Element

class Command(BaseCommand):
    help = 'Supprime tous les éléments de la base de données'

    def handle(self, *args, **kwargs):
        count = Element.objects.count()
        Element.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Tous les {count} éléments ont été supprimés avec succès !"))