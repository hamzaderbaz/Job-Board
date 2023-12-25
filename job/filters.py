import django_filters
from .models import Job

# Filter class for Job model
class JobFilter(django_filters.FilterSet):
    
    # Filter for job descriptions containing specific text
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job  # Specifies the model to be filtered
        fields = '__all__'  # Includes all fields of the Job model for filtering
        exclude = ['owner', 'published_at', 'image', 'salary', 'vacancy', 'slug'] # Excludes specific fields from being used for filtering
