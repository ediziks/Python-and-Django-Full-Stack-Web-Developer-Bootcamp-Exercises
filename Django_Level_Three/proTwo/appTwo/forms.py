from django import forms
from django.core import validators
from appTwo.models import Users


class User(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Confirm Email')
  
  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    vmail = all_clean_data['verify_email']

    if email != vmail:
      raise forms.ValidationError('Make Sure Emails Match!')

class UserForm(forms.ModelForm):
  class Meta:
    model = Users
    fields = ['name', 'email']
