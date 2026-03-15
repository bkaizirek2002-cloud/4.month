from django import forms
from .models import ITSpecialist
from captcha.fields import CaptchaField

class ITSpecialistForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ITSpecialist
        fields = '__all__'
        widgets = {
            'birth_date':
forms.DateInput(attrs={'type': 'date'}),
        }