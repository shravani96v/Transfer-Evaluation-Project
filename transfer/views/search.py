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
from ..forms import SchoolForm
from django.http import HttpResponse
import json as simplejson
from django.core.paginator import Paginator


def search(request):
    schools = School.objects.all()
    major = Major.objects.all()
    transfereval = Transferevaluation.objects.all()
    # transfereval.paginate(page=request.GET.get("page", 1), per_page=20)
    paginator = Paginator(transfereval, 5)
    page_number = request.GET.get('page')


    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        majorid = request.POST.get("major")
        schoolid = request.POST.get("school_id")

        if majorid == "null" and schoolid == "null":
            transfereval = Transferevaluation.objects.all()
            paginator = Paginator(transfereval, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            print(page_obj)
            return render(request, 'home_paginated.html', {"major": major, "schools": schools, "transfereval": transfereval, 'page_obj': page_obj})
        elif majorid == "null" and schoolid != "null":
           school = School.objects.filter(school_id=schoolid)
           course = TransferCourse.objects.filter(school_id__in = school)
           transfereval = Transferevaluation.objects.filter(transfer_course_id__in = course)
           paginator = Paginator(transfereval, 10)
           page_number = request.GET.get('page')
           page_obj = paginator.get_page(page_number)

           return render(request, 'home_paginated.html', {"major": major, "schools": schools, 'page_obj': page_obj})
        elif majorid != "null" and schoolid == "null":
           major_filter = Major.objects.filter(major_id=majorid)
           major_req = Major_requirement.objects.filter(major_id__in=major_filter)
           transfereval = Transferevaluation.objects.filter(major_req_id__in = major_req)
           paginator = Paginator(transfereval, 10)
           page_number = request.GET.get('page')
           page_obj = paginator.get_page(page_number)



           return render(request, 'home_paginated.html', {"major": major, "schools": schools, 'page_obj': page_obj})
        else:
           school = School.objects.filter(school_id=schoolid)
           course = TransferCourse.objects.filter(school_id__in = school)
           major_filter = Major.objects.filter(major_id=majorid)
           major_req = Major_requirement.objects.filter(major_id__in=major_filter)

           major_transfereval = Transferevaluation.objects.filter(major_req_id__in = major_req).filter(transfer_course_id__in = course)
           paginator = Paginator(major_transfereval, 10)
           page_number = request.GET.get('page')
           page_obj = paginator.get_page(page_number)
           return render(request, 'home_paginated.html', {"major": major, "schools": schools, 'page_obj': page_obj})
    return render(request, 'home_paginated.html', {"major": major, "schools": schools, "page_obj": page_obj, 'page_number':page_number})


def search_ajax(request):
    school = []
    majorid = request.GET.get('id', None)

    major = Major.objects.filter(major_id=majorid)
    major_req = Major_requirement.objects.filter(major_id__in=major)
    major_transfereval = Transferevaluation.objects.filter(major_req_id__in = major_req)
    for major_transfereval in major_transfereval:
        if {'name': major_transfereval.school(), 'id': major_transfereval.schoolid()} not in school:
            school.append({'name': major_transfereval.school(), 'id': major_transfereval.schoolid()})
    # schools should be filtered with majors
    return HttpResponse(simplejson.dumps(school), content_type='application/json')


def search_ajax2(request):
    major = []
    schoolid = request.GET.get('id', None)

    school = School.objects.filter(school_id=schoolid)
    course = TransferCourse.objects.filter(school_id__in = school)
    school_transfereval = Transferevaluation.objects.filter(transfer_course_id__in = course)
    for school_transfereval in school_transfereval:
        if {'name': school_transfereval.major(), 'id': school_transfereval.majorid()} not in major:
            major.append({'name':  school_transfereval.major(), 'id': school_transfereval.majorid()})
    # schools should be filtered with majors
    return HttpResponse(simplejson.dumps(major), content_type='application/json')
