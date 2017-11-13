from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        data = self.cleaned_data['email']
        ubmail = data.split('@')[1]
        if "@buffalo.edu" not in ubmail:
            raise forms.ValidationError("Must enter a UB email address")
        return data
