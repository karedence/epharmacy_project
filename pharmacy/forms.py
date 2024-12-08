from django import forms
from .models import Pharmacy, Medicine 



class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = ['name', 'location', 'phone_number']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'quantity', 'price', 'description', 'pharmacies']


class MedicineSearchForm(forms.Form):
    search_query = forms.CharField(label='Search for a Medicine', max_length=200)

