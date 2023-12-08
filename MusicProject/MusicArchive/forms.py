from django.forms import ModelForm
from .models import Satisfaction

class FeedbackForm(ModelForm):
    class Meta:
        model = Satisfaction
        fields = [
            'feedback',
            'rating'
        ]
