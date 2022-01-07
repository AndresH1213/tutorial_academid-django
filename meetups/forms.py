from django import forms
from .models import Participant

'''forms.ModelForm can be convenient if u wanna infer a form from a model and then use the .save(). But we
can also build a form object which give us all the validation logic and so on with forms.Form -> with that we have to
define all the form fields on our own'''
class RegistrationsForm(forms.Form):
    email = forms.EmailField(label='Your email')
    # class Meta:
    #     model = Participant
    #     fields = ['email']