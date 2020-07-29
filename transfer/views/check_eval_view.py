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
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from ..forms import CheckEvaluationForm


def check_evaluation(request):
    """
    major_name_list = []
    for major_name in Major:
        major_name_list.append(major_name.major_name)
    """
    form = CheckEvaluationForm()

    if request.method == 'POST':
        form = CheckEvaluationForm(request.POST)
        if form.is_valid():
            # adding data to checkevalution model
            check = form.save()
            # check_id = check.check_eval_id
            return render(request, 'check_eval_html/check_validation.html', {'check': check})

    return render(request, 'check_eval_html/check_eval.html', {'form': form})
