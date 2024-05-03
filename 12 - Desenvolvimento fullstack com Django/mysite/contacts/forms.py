from django import forms

from .models import Contact


class NameForm(forms.Form):
    your_name = forms.CharField(label="Seu nome", max_length=100)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
