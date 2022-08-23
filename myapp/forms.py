from dataclasses import fields
from pyexpat import model
from django import forms
from .models import user_signup,notes,contact

class SignupForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'

class NotesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'


