from django.contrib import admin
from .models import Element

# Register your models here.

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('numero', 'symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col', 'electronegativite', 'etat', 'masse_volumique', 'point_fusion')
    list_editable = ('symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col', 'electronegativite', 'etat', 'masse_volumique', 'point_fusion')
    search_fields = ('numero', 'symbole', 'nom')
