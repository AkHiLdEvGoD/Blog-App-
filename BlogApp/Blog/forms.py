from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ("blog_area","image","title")

    
