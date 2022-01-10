from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(max_length=120) 
    description = forms.CharField() 
    price = forms.DecimalField(decimal_places=2, max_digits=500) 