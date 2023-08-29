from django import forms

class CarPredictionForm(forms.Form):
    mileage = forms.FloatField(label='Mileage')
    max_power = forms.FloatField(label='Max Power')
    year = forms.IntegerField(label='Year')
