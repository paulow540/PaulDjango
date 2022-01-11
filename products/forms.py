from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=120, widget=forms.TextInput(
                                    attrs={
                                        "placeholder":"Your title",   
                                    }
                                )) 
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                                    attrs={
                                        "class":"new-class-name two",   
                                    }
                                )) 
    price = forms.DecimalField(initial =199.9, decimal_places=2, max_digits=500) 
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(max_length=120, widget=forms.TextInput(
                                    attrs={
                                        "placeholder":"Your title",   
                                    }
                                )) 
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                                    attrs={
                                        "class":"new-class-name two",   
                                    }
                                )) 
    price = forms.DecimalField(initial =199.9, decimal_places=2, max_digits=500) 