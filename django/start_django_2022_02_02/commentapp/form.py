from dataclasses import field
from xml.etree.ElementTree import Comment
from django.forms import ModelForm
from commentapp.models import Comment

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']