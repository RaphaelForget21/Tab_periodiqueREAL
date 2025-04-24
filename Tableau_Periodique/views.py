from django.http import JsonResponse
from django.shortcuts import render
from .models import Element

def periodic_table_view(request):
    elements = Element.objects.all()
    return render(request, 'tab.html', {'elements': elements})

def get_elements_json(request):
    elements = Element.objects.all().values(
        'numero', 'symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col'
    )
    return JsonResponse(list(elements), safe=False)

