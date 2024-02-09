from django import forms

class contactForm(forms.Form):

    name=forms.CharField(label='Name', required=True)
    email=forms.CharField(label='Email', required=True)
    content=forms.CharField(label='Content', widget=forms.Textarea)