import json
from django.core.management.base import BaseCommand
from Tableau_Periodique.models import Element

class Command(BaseCommand):
    help = 'Load elements from JSON into the database'

    def handle(self, *args, **kwargs):
        with open('elements_clean.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            if Element.objects.filter(symbole=item['symbole']).exists():
                # verifie que element existe deja  dans DB
                self.stdout.write(self.style.WARNING(f"Element {item['symbole']} existe deja. sauté..."))
                continue
            Element.objects.create(
                numero=item.get('numero') or None,
                symbole=item['symbole'],
                nom=item['nom'],
                masse=item.get('masse') or None,
                categorie=item['categorie'],
                position_row=item['position']['row'],
                position_col=item['position']['col']
            )

        self.stdout.write(self.style.SUCCESS("Elements charges avec succes!"))
