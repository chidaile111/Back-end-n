from django import forms
from django.forms import fields
from nguoidung.models import User

class CreateNewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name',
            'nation',
            'dateofbirth',
            'email',
            'gender'
        )