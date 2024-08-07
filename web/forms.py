from django import forms
from .models import ContactForm
from django.forms import ModelForm 

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Email',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(max_length=64, label = 'Nombre')
    message = forms.CharField(label='Mensaje')