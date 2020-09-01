from django import forms

from .models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'phone',
            'message',
            'address'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
