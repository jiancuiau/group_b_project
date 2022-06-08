from django import forms
from .models import LaborClass, SupplyClass, EquipmentClass


class NewLaborFormUsingModelForm(forms.ModelForm):
    class Meta:
        model = LaborClass
        fields = "__all__"
        labels = {'labor_class': "Labor Class", 'billing_code': 'Billing Codes'}
        # help_texts = {'name': 'Provide a unique name of the Course'}
        # widgets = {'description': forms.Textarea(attrs={'cols': 100, 'rows': 4})}


class NewSupplyFormUsingModelForm(forms.ModelForm):
    class Meta:
        model = SupplyClass
        fields = "__all__"
        labels = {'supply_class': "Supply Class", 'billing_code': 'Billing Codes'}
        # help_texts = {'name': 'Provide a unique name of the Course'}
        # widgets = {'description': forms.Textarea(attrs={'cols': 100, 'rows': 4})}


class NewEquipmentFormUsingModelForm(forms.ModelForm):
    class Meta:
        model = EquipmentClass
        fields = "__all__"
        labels = {'equip_class': "Equipment Class", 'billing_code': 'Billing Codes'}
