from django import forms
from django.forms import ModelForm
from .models import *
from .fields import ListTextWidget
from crispy_forms.helper import FormHelper

class CourseForm1(ModelForm):
    class Meta:
        model = TransferCourse
        fields = ['transfer_course_id', 'subject_number']


class ApproverForm(ModelForm):
    class Meta:
        model = Approver
        fields = ['approver_name']


class SchoolForm(forms.Form):
    school = forms.CharField(required=True)
    def __init__(self, *args, **kwargs):
        _school_list = kwargs.pop('data_list', None)
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.fields['school'].widget = ListTextWidget(data_list=_school_list, name='school-list')


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
        fields = ['transfer_course_id', 'major_req_id','sem_year_taken']

class DateInput(forms.DateInput):
    input_type = 'date'


class CheckEvaluationForm(ModelForm):
    class Meta:
        model = CheckEvaluation
        exclude = ['check_eval_id', 'major_name', 'school_name']
        widgets = {
            'expiration_date': DateInput(),
        }
