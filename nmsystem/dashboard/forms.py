from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categorietype, Product, Customer


class Categorietypeform(forms.ModelForm):
    class Meta:
        model = Categorietype
        fields = [
            'title',
            'status_choice',

        ]


class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'Brand', 'Model', 'colour', 'description', 'status', 'categorietype'
        ]


class Creatuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
