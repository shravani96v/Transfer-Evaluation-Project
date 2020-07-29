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
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
import json as simplejson


def state_search(request):
    if request.method == "POST":
        schoolid = request.POST.get("school")

        school = School.objects.filter(school_id=schoolid)
        transfercourse = TransferCourse.objects.filter(school_id__in=school)
        print(school)
        print(transfercourse)
        transfereval = Transferevaluation.objects.filter(transfer_course_id__in=transfercourse)
        print(transfereval)
        return render(request, 'transferevaluation_html/transfereval_home.html', {'object_list': transfereval})

    return render(request, 'searchbystate.html')


def searchstate_ajax(request):
    school_list = []
    schoolid = request.GET.get('id', None)

    schools = School.objects.filter(state_name = schoolid)
    print(schools)
    for school in schools:
        if {'name': school.name(), 'id': school.schoolid()} not in school_list:
            school_list.append({'name': school.name(), 'id': school.schoolid()})
    return HttpResponse(simplejson.dumps(school_list), content_type='application/json')
