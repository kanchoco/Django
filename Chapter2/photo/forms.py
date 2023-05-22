from django import forms
from .models import Photo

# Django의 ModelForm을 상속
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = (
            'title',
            'author',
            'image',
            'description',
            'price',
        )