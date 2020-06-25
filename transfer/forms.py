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
