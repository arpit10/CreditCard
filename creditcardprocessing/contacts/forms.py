from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text="100 Characters max.")
    email = forms.EmailField(required=True, max_length=100)
    comment = forms.CharField(required=True, widget=forms.Textarea)