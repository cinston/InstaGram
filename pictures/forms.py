from django import forms
from .models import image

UploadForm(forms.ModelForms):
class Meta:
    model = Image 
    field = ('pic','desctiption')
