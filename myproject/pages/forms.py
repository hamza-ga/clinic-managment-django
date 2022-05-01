from django import forms
from .models import Consaltations ,Prescription

class ConsaltationsForm(forms.ModelForm):
    class Meta:
        model = Consaltations
        fields = ('category','patient','doctor','disease_symptoms', 'history','x_rays_else', 'is_reconsult')
        widgets = {
            'category': forms.TextInput(attrs= {'class': 'form-control' ,'value': '', 'id': 'category', 'type':'hidden' }),
            'patient': forms.TextInput(attrs= {'class': 'form-control','value': '', 'id': 'patient', 'type':'hidden' }),
            'doctor': forms.TextInput( attrs= {'class': 'form-control','value': '','id': 'doctor', 'type':'hidden' }),
            'disease_symptoms': forms.Textarea(attrs= {'class': 'form-control'}),
            'history': forms.Textarea(attrs= {'class': 'form-control'}),
            'is_reconsult': forms.CheckboxInput(),
        }   

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('doctor_name','patient_name','consult_id','body','re_prescription_date')
        widgets = {
            'doctor_name': forms.TextInput(attrs= {'class': 'form-control','value': '', 'id': 'doctor', 'type':'hidden' }),
            'patient_name': forms.TextInput( attrs= {'class': 'form-control','value': '','id': 'patient', 'type':'hidden' }),
            'consult_id': forms.TextInput( attrs= {'class': 'form-control','value': '','id': 'consult_id', 'type':'hidden' }),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            're_prescription_date': forms.DateInput(attrs= {'class': 'form-control'}),
        }   
