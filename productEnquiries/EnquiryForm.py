from django import forms
from .models import productEnquiries


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = productEnquiries
