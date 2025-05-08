from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Element, ElementNote
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm
import json
from django.views.decorators.csrf import csrf_exempt


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
            return redirect('periodic_table')  # Redirect on successful login
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")  # Add error message
    return render(request, 'login.html')

def periodic_table_view(request):
    elements = Element.objects.all()
    return render(request, 'tab.html', {'elements': elements, 'is_authenticated': request.user.is_authenticated})

def get_elements_json(request):
    elements = Element.objects.all().values(
        'numero', 'symbole', 'nom', 'masse', 'categorie', 'position_row', 'position_col', 'electronegativite', 'etat','masse_volumique', 'point_fusion'
    )
    return JsonResponse(list(elements), safe=False)

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

@login_required
@csrf_exempt
def save_note_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        element_id = data.get('element_id')
        note = data.get('note')

        if not element_id or not note:
            return JsonResponse({'success': False, 'error': 'Invalid data'})

        # Save or update the note for the specific user and element
        ElementNote.objects.update_or_create(
            user=request.user,
            element_id=element_id,
            defaults={'note': note}
        )
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
@login_required
def get_note_view(request):
    element_id = request.GET.get('element_id')

    if not element_id or not element_id.isdigit():
        return JsonResponse({'success': False, 'error': 'Invalid or missing element_id'})

    try:
        element_note = ElementNote.objects.get(user=request.user, element_id=int(element_id))
        return JsonResponse({'success': True, 'note': element_note.note})
    except ElementNote.DoesNotExist:
        return JsonResponse({'success': True, 'note': ''})  # Return empty note if not found
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
@csrf_exempt
def delete_note_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            element_id = data.get('element_id')

            if not element_id or not isinstance(element_id, int):
                return JsonResponse({'success': False, 'error': 'Invalid or missing element_id'})

            # Delete the note
            deleted, _ = ElementNote.objects.filter(user=request.user, element_id=element_id).delete()
            if deleted:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Note not found'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})