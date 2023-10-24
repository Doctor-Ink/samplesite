from django.forms import ModelForm

from .models import BB


class BbForm(ModelForm):
    class Meta:
        model = BB
        fields = ('title', 'content', 'price', 'rubric')
