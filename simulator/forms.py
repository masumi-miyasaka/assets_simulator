from django import forms

class AssetForm(forms.Form):
    initial_asset = forms.IntegerField(label='Intial Asset', initial=1000000)
    interest_rate = forms.FloatField(label='Interest Rate (decimal)', initial=0.05)
    inflation_rate = forms.FloatField(label='Inflation Rate (decimal)', initial=0.02)
    years = forms.IntegerField(label='Years', initial=10)