from django import forms
from django.forms import ModelForm
from django.core.validators import validate_email
from .validators import name_validator, ValidationError
from .models import Clients

class SearchClientForm(forms.Form):
    search_field = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}))

# class RegistrationForm(forms.Form):
#     first_name_field = forms.CharField(label="First name", validators=[name_validator])
#     last_name_field = forms.CharField(label="Last name", validators=[name_validator])
#     dob_field = forms.DateField(label="Date of birth", widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
#     address_field = forms.CharField(label="Address")
#     phone_field = forms.CharField(label="Phone number")
#     email_field = forms.CharField(label="Email", validators=[validate_email])


class RegistrationForm(ModelForm):   
    class Meta:
        model = Clients
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
        }
        help_texts = {
            'first_name': 'Only latin letters.'
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone)<7:
            raise ValidationError('Enter a valid phone number.')
        elif Clients.objects.filter(phone=phone):
            raise ValidationError('This phone number is already registered.')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Clients.objects.filter(email=email):
            raise ValidationError('This email is already registered.')
        return email