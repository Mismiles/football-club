from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your full name', required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=250)