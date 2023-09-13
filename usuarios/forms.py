from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Usuario
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    grupo = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2', 'grupo']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class PasswordResetRequestForm(forms.Form):
    correo = forms.EmailField()

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        try:
            Usuario.objects.get(email=correo)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("Este correo electrónico no está registrado en nuestro sistema.")
        return correo