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
from ..forms import CheckEvaluationForm


def check_post_evaluation(request, check_eval_id):
    if request.method == 'POST':
            check = CheckEvaluation.objects.get(check_eval_id = check_eval_id)
            schools = School.objects.filter(school_name=check.school_name)
            major = Major.objects.filter(major_name=check.major_name)
            approver = Approver.objects.filter(approver_name=check.approver_name)


            # Addition of new school and its course from form
            if len(schools) == 0:
                School(school_name=check.school_name, state_name='None').save()
                # CheckEvaluation(school_name=check.school_name).save()
                school = School.objects.get(school_name=check.school_name)
                TransferCourse(school_id=school, subject_number=check.transfer_subject_number, title=check.transfer_course_title).save()
            else:
                # Addition of new courses if school exists in School model
                course = TransferCourse.objects.filter(school_id__in = schools).filter(subject_number=check.transfer_subject_number)
                if len(course) == 0:
                    school = School.objects.get(school_name=check.school_name)
                    TransferCourse(school_id=school, subject_number=check.transfer_subject_number, title=check.transfer_course_title).save()


            #Adding new majors and its major_requirements to its models
            if len(major) == 0:
                Major(major_name=check.major_name).save()
                new_major = Major.objects.get(major_name=check.major_name)
                Major_requirement(description=check.unhm_equivalent, major_id=new_major).save()
            else:
                # addition of new major_requirement if the major already exists in the Major model
                major = Major_requirement.objects.filter(major_id__in=major).filter(description=check.unhm_equivalent)
                if len(major) == 0:
                    new_major = Major.objects.get(major_name=check.major_name)
                    Major_requirement(description=check.unhm_equivalent, major_id=new_major).save()

            # addition of new approver
            if len(approver) == 0:
                Approver(approver_name = check.approver_name).save()
                # else

            school = School.objects.filter(school_name=check.school_name)
            transfer_course = TransferCourse.objects.filter(school_id__in = school).filter(subject_number = check.transfer_subject_number)

            major = Major.objects.filter(major_name = check.major_name)
            major_req = Major_requirement.objects.filter(major_id__in = major).filter(description=check.unhm_equivalent)

            transfer_eval = Transferevaluation.objects.filter(major_req_id__in = major_req).filter(transfer_course_id__in = transfer_course)
            if len(transfer_eval) == 0:
                for each_transfer_course in transfer_course:
                    transfer_course = each_transfer_course
                    print(transfer_course)

                transfer_course.title = check.transfer_course_title

                for new_major_req in major_req:
                    major_req = new_major_req
                    print(major_req)

                Transferevaluation(
                        transfer_course_id=transfer_course,
                        major_req_id=major_req,
                        sem_year_taken=check.sem_or_year_taken,
                        expiration_date=check.expiration_date,
                        approved_status=check.approved_status,
                        approver_id=Approver.objects.get(
                                approver_name=check.approver_name
                            )
                    ).save()
            object_list = Transferevaluation.objects.all()

    return render(request, 'transferevaluation_html/transfereval_home.html', {'object_list': object_list})
