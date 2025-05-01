from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Nom d'utilisateur",
        help_text="Requis. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ uniquement."
    )
    email = forms.EmailField(
        label="Adresse e-mail",
        help_text="Veuillez entrer une adresse e-mail valide."
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        help_text="Votre mot de passe doit contenir au moins 8 caractères."
    )
    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput,
        help_text="Entrez le même mot de passe pour confirmation."
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]