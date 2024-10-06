from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Select

from core.models import GroupMember


class RegistrationForm(forms.ModelForm):
    """
      Form for Registering new users
    """

    # email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = GroupMember
        fields = ('title','firstname', 'othernames', 'lastname', 'email', 'address', 'phone', 'occupation', 'position')
        widgets = {
            'title': Select(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}),
            'othernames': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Other Names',}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address',}),
            'phone': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number',
                    'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}',
                    'minlength': 10,
                    'maxlength': 10,
                }),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation',}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email',}),
            'position': Select(attrs={'class': 'form-control'}),
        }