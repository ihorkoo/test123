from django.forms import ModelForm, Textarea
from . import models


class AddPost(ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'text', "author"]
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
