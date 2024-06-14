# myapp/forms.py
from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['first_name', 'last_name', 'email', 'date_of_birth','address','nationality','gender','emergency_name','emergency_phone','emergency_email','id_mark','b_group','identity_mark','date_admission','prefer_lan','father_occu','mother_occu','income','extra_activities','photo','proof_address','identity']
