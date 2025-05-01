from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Element,ElementNote
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Utilisateur crée avec succès!")
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('periodic_table')  # Redirect to the periodic table page
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')
def periodic_table_view(request):
    elements = Element.objects.all()
    return render(request, 'tab.html', {'elements': elements})

def get_elements_json(request):
    elements = Element.objects.all().values(
        'numero', 'symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col'
    )
    return JsonResponse(list(elements), safe=False)

def logout_view(request):
    logout(request)
    return redirect('login')# Redirect to the login page after logout

@login_required
def save_note_view(request):
    if request.method == 'POST':
        element_id = request.POST['element_id']
        note_text= request.POST['note']
        element= Element.objects.get(id=element_id)
        note, created= ElementNote.objects.get_or_create(user=request.user, element=element)
        note.note= note_text
        note.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
@login_required
def get_note_view(request):
    element_id = request.GET.get('element_id')
    element = Element.objects.get(id=element_id)
    note = ElementNote.objects.filter(user=request.user, element=element).first()
    return JsonResponse({'note': note.note if note else ''})
