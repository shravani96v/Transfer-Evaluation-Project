from ..models.model_major import Major
from ..models.model_school import School
from ..models.model_course import Course
from ..models.model_major_requirement import Major_requirement
from ..models.model_transferevaluation import Transferevaluation
from ..models.model_approver import Approver

from django.shortcuts import render, get_object_or_404


def remove_all_data(request):
    Major.objects.all().delete()
    School.objects.all().delete()
    Course.objects.all().delete()
    Major_requirement.objects.all().delete()
    Transferevaluation.objects.all().delete()
    Approver.objects.all().delete()
    return render(request, 'home.html')
