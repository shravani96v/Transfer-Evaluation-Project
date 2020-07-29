from django.http import HttpResponse
from ..models import School, Approver, TransferCourse, Major_requirement, Major, School, Transferevaluation
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..forms import CourseForm1, ApproverForm, MajorForm, SchoolForm, TransferevaluationForm, MajorRequirementForm


def create_all(request):
    course_form = CourseForm1()
    approver_form = ApproverForm()
    major_form = MajorForm()
    school_form = SchoolForm()
    transfereval_form = TransferevaluationForm()
    major_requirement_form = MajorRequirementForm()
    return render(request, "create_all.html", {"course_form": course_form, "approver_form": approver_form , "major_form": major_form, "school_form": school_form, "transfereval_form": transfereval_form, "major_requirement_form": major_requirement_form})


# "approver_form": approver_form , "major_form": major_form, "school_form": school_form, "transfereval_form": transfereval_form, "major_requirement_form": major_requirement_form})
