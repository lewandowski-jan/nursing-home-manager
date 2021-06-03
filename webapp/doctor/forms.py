from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from database.models import KartyZdrowia, PrzyjmowaneLeki

class FormHealthCard(forms.ModelForm):
    class Meta:
        model = KartyZdrowia
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Zapisz', css_class='btn-info'))
        self.helper.layout = Layout(
                Row(
                    Column('grupa_krwi'),
                    Column('czynnik_rh'),
                ),
                Row(
                    Column('uczulenia')
                ),
                Row(
                    Column('choroby')
                ),
            )

class FormAssignedMedicine(forms.ModelForm):
    class Meta:
        model = PrzyjmowaneLeki
        fields = "__all__"
        exclude=['karta_zdrowia']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_od'] = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
        self.fields['data_do'] = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Dodaj', css_class='btn-info'))
        self.helper.layout = Layout(
            Row(
                Column('lek'),
            ),
            Row(
                Column('data_od'),
                Column('data_do'),
            ),
            Row(
                Column('dawka')
            ),
            Row(
                Column('czestotliwosc')
            ),
        )