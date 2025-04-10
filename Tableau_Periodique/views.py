
from django.shortcuts import render
from .models import Element

def periodic_table_view(request):
    elements = Element.objects.all()
    return render(request, 'tab.html', {'elements': elements})
