from django import forms
from .models import leave_application
from ckeditor.widgets import CKEditorWidget

class leave_applications(forms.ModelForm):
    

    class Meta:
        model=leave_application
        fields='__all__'
        exclude=['user','applied_on','approved','total_days']





        
        # widgets = {
	    #     'title': forms.TextInput(attrs={'class': 'input','placeholder':'Title'})
        # }
        
    # start_date = forms.DateField(
    #     widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
    #     input_formats=('%m/%d/%Y', )
    #     )
    # end_date=forms.DateField(
    #     widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
    #     input_formats=('%m/%d/%Y', )
    #     )