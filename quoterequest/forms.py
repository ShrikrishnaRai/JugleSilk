from django import forms

from .models import QuoteRequest


class QuoteReuqestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = (
            'fullName',
            'email',
            'description',
            'categories'
        )
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.TextInput(attrs={'class': 'form-control'}),
        }
