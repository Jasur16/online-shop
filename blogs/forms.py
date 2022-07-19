from django import forms
from .models import CommentModel

class CommentModelForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        exclude = ['created_at', 'post']