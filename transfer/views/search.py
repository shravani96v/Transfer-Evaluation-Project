from ..models.model_major import Major
from ..models.model_school import School
from django.shortcuts import render
from django.views.generic import ListView


class SearchByMajor(ListView):
    model = Major
    template_name = 'searchbymajor.html'
    context_object_type = 'object_list'


def searchbyschool(request):
    name = School.objects.all()
    return render(request, 'searchbyschool.html', {"School": name})
