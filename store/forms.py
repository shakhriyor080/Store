from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", required=True, widget=forms.TextInput(attrs={'class':'input margin-b-20'}))
    password1 = forms.CharField(label="Parol", required=True, widget=forms.PasswordInput(attrs={'class': 'input margin-b-20'}))
    password2 = forms.CharField(label="Takroriy parol", required=True, widget=forms.PasswordInput(attrs={'class': 'input margin-b-20'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class':'input margin-b-20'}))

    class Meta:
        model = User

        fields = ("email", "username","password1","password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]

        if commit:
            user.save()
        return user
