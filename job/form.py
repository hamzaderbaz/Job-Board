from django import forms
from .models import Apply, Job

# Form for applying to a job
class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply  # Specifies the model for which the form is created
        fields = ['name', 'email', 'website', 'CV', 'cover_letter']  # Fields to be included in the form

# Form for adding a new job
class JobForm(forms.ModelForm):
    class Meta:
        model = Job  # Specifies the model for which the form is created
        fields = '__all__'  # Includes all fields from the Job model in the form
        exclude = ('slug', 'owner')  # Excludes 'slug' and 'owner' fields from the form
