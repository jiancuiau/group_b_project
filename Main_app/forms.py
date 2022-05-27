from django import forms
from .models import LaborClass


class NewLaborFormUsingModelForm(forms.ModelForm):
    class Meta:
        model = LaborClass
        fields = "__all__"
        labels = {'labor_class': "Labor Class", 'billing_code': 'Billing Codes'}
        # help_texts = {'name': 'Provide a unique name of the Course'}
        # widgets = {'description': forms.Textarea(attrs={'cols': 100, 'rows': 4})}