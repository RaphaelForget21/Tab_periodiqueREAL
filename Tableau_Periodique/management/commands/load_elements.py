import json
from django.core.management.base import BaseCommand
from Tableau_Periodique.models import Element

class Command(BaseCommand):
    help = 'Load elements from JSON into the database'

    def handle(self, *args, **kwargs):
        with open('elements_clean.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            # Check and delete existing element by 'numero'
            if Element.objects.filter(numero=item['numero']).exists():
                self.stdout.write(self.style.WARNING(f"Element with numero {item['numero']} already existed"))
                continue

            # Create a new element
            Element.objects.create(
                numero=item.get('numero') or None,
                symbole=item['symbole'],
                nom=item['nom'],
                masse=item.get('masse') or None,
                categorie=item['categorie'],
                position_row=item['position']['row'],
                position_col=item['position']['col'],
                electronegativite=item.get('electronegativite') or None,
                etat=item['etat'],
                masse_volumique=item.get('masse_volumique') or None,
                point_fusion=item.get('point_fusion') or None
            )

        self.stdout.write(self.style.SUCCESS("Elements loaded successfully!"))