from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from database.models import Seniorzy, KartyZdrowia, Leki

class NewSenior(forms.ModelForm):
    class Meta:
        model = Seniorzy
        fields = "__all__"
        exclude = ['karty_zdrowia']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Utwórz seniora', css_class='btn-info'))

class NewCard(forms.ModelForm):
    class Meta:
        model = KartyZdrowia
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Utwórz kartę zdrowia', css_class='btn-info'))

class FormMedicine(forms.ModelForm):
    class Meta:
        model = Leki
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Zapisz', css_class='btn-info')) 