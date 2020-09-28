from django import forms
from django.forms import ModelForm, Form
from .models import Post

class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ["author","title","description"]