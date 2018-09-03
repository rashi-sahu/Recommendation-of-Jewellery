from django import forms
from django.forms import ModelForm
from jewellery.fields import CameraImageField
from fractions import Fraction

class ProfileForm(forms.Form):
   #name = forms.CharField(max_length = 100)
   picture = forms.ImageField()
   #landscape = CameraImageField(aspect_ratio=Fraction(16, 9))
   #image_data = forms.CharField(widget=forms.HiddenInput(), required=False)
