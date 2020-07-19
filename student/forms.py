from django import forms
import re
from student.models import StudentModel

class RegisterForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
def check_name(self):
    name = self.cleaned_data["name"]
    res = re.findall(r"^[A-Z a-z]*$",name)
    print(name)
    if res:
        return name
    else:
        raise forms.ValidationError("Invalid Name")
def check_contact(self):
    contact = self.cleaned_data["contactno"]
    cno = re.findall(r"[7-9]{1}[0-9]{9}",contact)
    if cno:
        return contact
    else:
        raise forms.ValidationError("Invalid Contact")