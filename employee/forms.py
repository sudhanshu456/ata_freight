from django import forms
from .models import leave_application
from ckeditor.widgets import CKEditorWidget

class leave_applications(forms.ModelForm):
    class Meta:
        model=leave_applications
        fields='__all__'
        # widgets = {
	    #     'title': forms.TextInput(attrs={'class': 'input','placeholder':'Title'})
        # }
        