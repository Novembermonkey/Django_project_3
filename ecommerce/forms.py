from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    receivers = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
