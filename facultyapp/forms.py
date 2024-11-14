from django import forms
from .models import AddCourse

from django import forms
from .models import StudentList

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student', 'course', 'section']

from .models import Marks
class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'course', 'marks']