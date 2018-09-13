from django import forms

from .models import account

class DocumentForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('username', 'parentname', 'childname', 'userid', 'email', 'image', )