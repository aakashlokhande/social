from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class UserRegisterForm (UserCreationForm):
    
    class Meta :
        model=User
        fields=['first_name','last_name','email','mobile_number','profile_pic', 'password1','password2']
    
    #check if mobile numbe doesnt contain character
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        for char in mobile_number:
            if char<'0' or char >'9':
                raise ValidationError(
                _('%(mobile_number)s is not a valid phone number'),
                params={'mobile_number': mobile_number},
                )
        return mobile_number