from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_type', 'produced_by', 'ingredients', 'weight',
                  'calories', 'proteins', 'carbohydrates', 'fat', 'fibre', 'salt',
                  'calories_per100', 'proteins_per100', 'carbohydrates_per100', 'fat_per100',
                  'fibre_per100', 'salt_per100', 'tags',
                  'product_image', 'additional_image', 'miniature_image')
        TYPE_CHOICES = [('0', '-- Wybierz Typ Produktu --'),
                        ('1', 'naturalne'),
                        ('2', 'przetworzone')]
        widgets = {
            'product_type': forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
