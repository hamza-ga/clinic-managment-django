from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import  Patient


class SignUpPatientForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'class': 'form-control'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    

    class Meta:
        model = Patient
        fields = ('username','first_name','last_name','email','password1','password2', 'birthday','phone_number')
    
    def __init__(self, *args, **kwargs):
        super(SignUpPatientForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs= {'class': 'form-control'}
        self.fields['password1'].widget.attrs= {'class': 'form-control'}
        self.fields['password2'].widget.attrs= {'class': 'form-control'}


class EditPatientForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'class': 'form-control'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = ('username','first_name','last_name','email','password' ,'birthday','phone_number')