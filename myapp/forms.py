from django import forms
from myapp.models import Student



class StudentAddForm(forms.ModelForm):
    
    class Meta:
        
        model=Student
        
        exclude=["id","created_date", "updated_date", "is_active"]