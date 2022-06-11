from .models import *
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'technologies']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['design_rating', 'content_rating', 'usability_rating']

