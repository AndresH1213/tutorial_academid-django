from django import forms
from .models import Participant

'''forms.ModelForm can be convenient if u wanna infer a form from a model and then use the .save(). But we
can also build a form object which give us all the validation logic and so on with forms.Form -> with that we have to
define all the form fields on our own'''
class RegistrationsForm(forms.Form):
    email = forms.EmailField(label='Your email')
    '''
    Use a modelform is kind of redundant here because we are not using the save method anymore
    model form is forms.modelForm this is convenient if we want to infere a form from a model and use the
    save method. But we can also build a form object with all the validation login and so on with forms.Form
    '''
    # class Meta:
    #     model = Participant
    #     fields = ['email']