from django import forms

from .models import QuoteRequest


class QuoteReuqestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = [
            'fullName',
            'email',
            'description',
            'categories'
        ]
