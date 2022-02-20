
from django.forms import ModelForm

from django.forms import ModelForm
from articleapp.models import Article
from django import forms

from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    contetnt = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left', 
                                                            'style': 'height: auto;'}))# WYSIWYG 사용하기 위해 추가된것
    
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    
    class Meta:
        model = Article
        fields = ['title', 'image','project', 'content']