from django.contrib import admin
from .models import Element

# Register your models here.

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('numero', 'symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col', 'atomic_radius', 'electronegativity', 'melting_point')
    list_editable = ('symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col', 'atomic_radius', 'electronegativity', 'melting_point')
    search_fields = ('numero', 'symbole', 'nom')
