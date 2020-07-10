from django import forms
import re
from app1.models import ClassModel

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassModel
        fields = ["course","faculty","date","time","fee","duration"]


