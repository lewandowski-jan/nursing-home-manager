from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from database.models import Seniorzy, KartyZdrowia, Leki, Pracownicy, Adresy, Poczty

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

class FormWorker(forms.ModelForm):
    class Meta:
        model = Pracownicy
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Zapisz', css_class='btn-info')) 

class FormSenior(forms.ModelForm):
    class Meta:
        model = Seniorzy
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Zapisz', css_class='btn-info')) 


class NewAddress(forms.ModelForm):
    class Meta:
        model = Adresy
        fields = "__all__"
        exclude = ['poczty']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Utwórz adres', css_class='btn-info'))

class NewPostal(forms.ModelForm):
    class Meta:
        model = Poczty
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Utwórz pocztę', css_class='btn-info'))

class NewWorker(forms.ModelForm):
    class Meta:
        model = Pracownicy
        fields = "__all__"
        exclude = ['adresy']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Utwórz pracownika', css_class='btn-info'))
        self.fields['data_zatrudnienia'] = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

class NewMedicine(forms.ModelForm):
    class Meta:
        model = Leki
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Utwórz lek', css_class='btn-info'))
