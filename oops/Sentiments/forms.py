from django import forms
from .models import attrition_upload


class attrition_form(forms.ModelForm):
    class Meta:
        model = attrition_upload
        fields = ('tables_id', 'user_name', 'file_name', 'file_upload')
        widgets = {'user_name': forms.HiddenInput()}