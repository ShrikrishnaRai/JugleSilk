from django import forms

from .models import ContactUs


class ContatctForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email',
            'phone',
            'message'
        ]

