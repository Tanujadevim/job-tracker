from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'status', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }