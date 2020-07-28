from django import forms

#Pode criar classe ou alguma coisa de forms
from products.models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']
