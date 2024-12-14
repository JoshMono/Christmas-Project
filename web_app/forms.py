from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, TextInput, ModelChoiceField, Form
from django.forms.utils import ErrorList
from .models import Person, Company

class CreatePersonForm(ModelForm):
    
    class Meta:
        
        model = Person
        fields = ["id", "first_name", "last_name", "email", "company"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = TextInput()
        self.fields["last_name"].widget = TextInput()

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data.get('first_name')) < 4:
            self.add_error('first_name', 'needs to be 4 or more')
        return cleaned_data
    
class CreateCompanyForm(ModelForm):
    
    class Meta:
        
        model = Company
        fields = ["id", "name", "industry"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget = TextInput()

class LinkPersonToCompanyForm(Form):

    people = ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        people = kwargs.pop("people")
        super().__init__(*args, **kwargs)
        self.fields["people"].queryset = people
