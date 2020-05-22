from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "text"]
        labels = {
            "user_name": "Your Name",
            "text": "Your Comment",
        }
