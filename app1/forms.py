from django import forms
import re
from app1.models import ClassModel

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassModel
        fields = ["name","faculty","date","time","fee","duration"]


