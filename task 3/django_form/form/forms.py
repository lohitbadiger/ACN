from django import forms 
from .models  import InfoStore 
# creating the forms fields for creating the new items for the website 


class AllInfoForm(forms.ModelForm):
    class Meta:
        model=InfoStore
        fields=[
            'name',
            'phone',
            'email'
        ]
