from django import forms
from django.forms import ModelForm
from .models import *


class CourseForm1(ModelForm):
    class Meta:
        model = TransferCourse
        fields = ['transfer_course_id', 'school_id', 'subject_number']


class ApproverForm(ModelForm):
    class Meta:
        model = Approver
        fields = ['approver_name']


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['state_name']


class MajorRequirementForm(ModelForm):
    class Meta:
        model = Major_requirement
        fields = ['description', 'major_id']


class MajorForm(ModelForm):
    class Meta:
        model = Major
        fields = ['major_name']


class TransferevaluationForm(ModelForm):
    class Meta:
        model = Transferevaluation
        exclude = ['transfer_eval_id']


class DropDownForm(forms.ModelForm):
    class Meta:
        model = DropDown
        fields = ('school', 'major')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['major'].queryset = Major.objects.none()



        if 'school' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['major'].queryset = DropDown.objects.filter(school_id=school_id).order_by('school')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['major'].queryset = self.instance.school.major_set.order_by('name')
