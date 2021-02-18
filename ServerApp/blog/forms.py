from django import forms

from .models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        widgets = {
            "content": forms.Textarea
        }
        fields = "__all__"
