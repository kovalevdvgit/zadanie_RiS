from django import forms
from bird.models import bird

class BirdForm(forms.ModelForm):

    class Meta:
        model = bird
        fields = '__all__'