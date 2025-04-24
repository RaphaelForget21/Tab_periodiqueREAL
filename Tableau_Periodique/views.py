from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Element
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "User created successfully!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
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

