from django import forms
from .models import *

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['image', 'phone_number', 'address', 'gender']
