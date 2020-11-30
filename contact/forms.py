from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text="100 characters max.")
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class MessageForm(forms.Form):
    name = forms.CharField(max_length=200,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter Username'
                               }))
    email = forms.CharField(max_length=200,
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Enter Your Email'
                            }))
    
    message = forms.CharField(max_length=1000,
                            widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Your Message'
                            }))
