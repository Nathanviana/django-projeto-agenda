from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    pictture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }
        )
    )
    
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome e último nome não podem ser iguais',
                code='invalid'
            )
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'admin':
            self.add_error(
                'first_name',
                ValidationError(
                    'Nome de usuário não permitido',
                    code='invalid'
                )
            )
        
        return first_name