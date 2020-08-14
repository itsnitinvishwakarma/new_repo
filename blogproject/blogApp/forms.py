
from django import forms

from blogApp.models import Comment


class EmailForm(forms.Form):
    Name=forms.CharField()
    by=forms.EmailField()
    to=forms.EmailField()
    comment=forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':6,'cols':25}))

class CommentForm(forms.ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={'rows':6,'cols':25}))

    class Meta:
        model=Comment
        fields=('name','email','body')

