from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']  # Remove 'user' from fields as it will be set in the view
