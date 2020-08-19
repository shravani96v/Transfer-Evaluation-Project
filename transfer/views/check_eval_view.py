from django.http import HttpResponse
from ..models import (
                     School,
                     CheckEvaluation,
                     Approver,
                     TransferCourse,
                     Major_requirement,
                     Major, School,
                     Approver,
                     TransferCourse,
                     Major_requirement,
                     Major,
                     School,
                     Transferevaluation
                     )
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
import json as simplejson
from ..forms import CheckEvaluationForm


def check_evaluation(request):
    """
    major_name_list = []
    for major_name in Major:
        major_name_list.append(major_name.major_name)
    """
    major = Major.objects.all()
    schools = School.objects.all()
    form = CheckEvaluationForm()

    if request.method == 'POST':
        form = CheckEvaluationForm(request.POST)
        if form.is_valid():
            # adding data to checkevalution model
            major_id = request.POST.get("major")
            major = Major.objects.get(major_id = major_id)
            school_id = request.POST.get("school_id")
            school = School.objects.get(school_id =school_id)
            approved_status = form.cleaned_data['approved_status']
            transfer_subject_number = form.cleaned_data['transfer_subject_number']
            transfer_course_title = form.cleaned_data['transfer_course_title']
            unhm_equivalent = form.cleaned_data['unhm_equivalent']
            approver_name = form.cleaned_data['approver_name']
            approved_status = form.cleaned_data['approved_status']
            sem_or_year_taken = form.cleaned_data['sem_or_year_taken']
            expiration_date = form.cleaned_data['expiration_date']

            check = CheckEvaluation(
                                   major_name=major.major_name,
                                   school_name=school.school_name,
                                   transfer_subject_number=transfer_subject_number,
                                   transfer_course_title=transfer_course_title,
                                   unhm_equivalent=unhm_equivalent,
                                   approver_name = approver_name,
                                   approved_status = approved_status,
                                   sem_or_year_taken = sem_or_year_taken,
                                   expiration_date = expiration_date
                                   )
            check.save()
            return render(request, 'check_eval_html/check_validation.html', {'check':check, 'major': major.major_name, 'school': school.school_name })

    return render(request, 'check_eval_html/check_eval.html', {'form': form, 'major': major, 'schools': schools})


def update_view(request, check_eval_id):
    # fetch the object related to passed id
    major = Major.objects.all()
    schools = School.objects.all()

    obj = CheckEvaluation.objects.get(check_eval_id = check_eval_id)

    check = CheckEvaluationForm(instance = obj)

    if request.method == 'POST':
        form = CheckEvaluationForm(request.POST)
        if form.is_valid():
            major_id = request.POST.get("major")
            major = Major.objects.get(major_id = major_id)
            school_id = request.POST.get("school_id")
            school = School.objects.get(school_id =school_id)
            approved_status = form.cleaned_data['approved_status']
            transfer_subject_number = form.cleaned_data['transfer_subject_number']
            transfer_course_title = form.cleaned_data['transfer_course_title']
            unhm_equivalent = form.cleaned_data['unhm_equivalent']
            approver_name = form.cleaned_data['approver_name']
            approved_status = form.cleaned_data['approved_status']
            sem_or_year_taken = form.cleaned_data['sem_or_year_taken']
            expiration_date = form.cleaned_data['expiration_date']
            CheckEvaluation.objects.filter(check_eval_id = check_eval_id).update(
                                                                                major_name=major.major_name,
                                                                                school_name=school.school_name,
                                                                                transfer_subject_number=transfer_subject_number,
                                                                                transfer_course_title=transfer_course_title,
                                                                                unhm_equivalent=unhm_equivalent,
                                                                                approver_name = approver_name,
                                                                                approved_status = approved_status,
                                                                                sem_or_year_taken = sem_or_year_taken,
                                                                                expiration_date = expiration_date
                                                                                )
            return render(request, 'check_eval_html/check_validation.html', {'check':CheckEvaluation.objects.get(check_eval_id = check_eval_id),  'major': major.major_name, 'school': school.school_name} )

    return render(request, "check_eval_html/check_eval.html", {'form': check, 'major': major, 'schools': schools, 'obj': obj})
