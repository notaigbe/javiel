from django.forms import TextInput, NumberInput, Textarea, Select, FileInput
from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Blog
        fields = ('category', 'title', 'slug', 'author', 'post', 'image', 'status')
        widgets = {
            'category': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'News Title', 'id': 'title'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug', 'id': 'slug', 'hidden': 'hidden'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Author', 'hidden': 'hidden'}),
            'post': Textarea(attrs={'class': "form-control w-100", 'placeholder': 'News Post'}),
            'image': FileInput(),
            'status': Select(attrs={'class': 'form-control'})
        }
