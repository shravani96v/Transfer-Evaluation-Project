from ..models.model_major import Major
from ..models.model_school import School
from ..models.model_transfer_course import TransferCourse
from ..models.model_major_requirement import Major_requirement
from ..models.model_transferevaluation import Transferevaluation
from ..models.model_approver import Approver
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect


def remove_all_data(request):

    if request.method == "POST":
        Major.objects.all().delete()
        School.objects.all().delete()
        TransferCourse.objects.all().delete()
        Major_requirement.objects.all().delete()
        Transferevaluation.objects.all().delete()
        Approver.objects.all().delete()
        return HttpResponseRedirect(reverse("home"))
    return render(request, 'removeall.html')
