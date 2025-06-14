from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from .models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    #LoginView passes request so you need to handle it
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(f'{email} not found')

        if len(password) < 8:
            raise forms.ValidationError('Password must have at least 8 characters')

        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError('Invalid email or password')

        self.user = user

        return cleaned_data

    def get_user(self):
        return self.user


class RegisterForm(forms.ModelForm):
    pass


# admin forms
class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'profile_pic',)