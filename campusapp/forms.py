from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import LostFoundItem


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]


class LostFoundItemForm(forms.ModelForm):

    class Meta:
        model = LostFoundItem

        fields = [
            'title',
            'item_type',
            'how_lost',
            'description',
            'location',
            'current_location',
            'latitude',
            'longitude',
            'date',
            'contact',
            'image',
            'estimated_cost',
            'status',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter item name',
                'class': 'form-control'
            }),

            'item_type': forms.Select(
                choices=[
                    ('Lost', 'Lost'),
                    ('Found', 'Found'),
                ],
                attrs={
                    'class': 'form-control'
                }
            ),

            'how_lost': forms.Textarea(attrs={
                'placeholder': 'How was the item lost/found?',
                'class': 'form-control',
                'rows': 3
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the item',
                'class': 'form-control',
                'rows': 4
            }),

            'location': forms.TextInput(attrs={
                'placeholder': 'Where was it lost/found?',
                'class': 'form-control'
            }),

            'current_location': forms.TextInput(attrs={
                'placeholder': 'Current location',
                'class': 'form-control'
            }),

            'latitude': forms.NumberInput(attrs={
                'placeholder': 'Latitude',
                'class': 'form-control',
                'step': 'any'
            }),

            'longitude': forms.NumberInput(attrs={
                'placeholder': 'Longitude',
                'class': 'form-control',
                'step': 'any'
            }),

            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'contact': forms.TextInput(attrs={
                'placeholder': 'Enter contact number',
                'class': 'form-control',
                'type': 'tel'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'estimated_cost': forms.NumberInput(attrs={
                'placeholder': 'Approximate cost',
                'class': 'form-control',
                'step': '0.01'
            }),

            'status': forms.Select(
                choices=[
                    ('Active', 'Active'),
                    ('Resolved', 'Resolved'),
                ],
                attrs={
                    'class': 'form-control'
                }
            ),
        }