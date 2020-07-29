from django.contrib import admin
from django.urls import path
from .views.major_requirement_views import *
from .views.course_views import *
from .views.major_views import *
from .views.school_views import *
from .views.transfer_evaluation_views import *
from .views.remove_data import *
from .views.approver_views import *
from .views.check_eval_view import *
from .views.load import *
from .views.major_requirement_views import *
# from .views.home import *
from .views.search import *
from .views.search_by_state_test import *
from .views.import_more import *
from .views.post_check_eval import *


urlpatterns = [
    #path('create', create_all, name = "create_all"),
    path('load-data/', import_file, name='import'),
    path('load-more/', import_more, name='import_more'),
    path('remove-data/', remove_all_data, name='remove_data'),
    path('home/', search, name='home'),
    path('search_ajax/', search_ajax, name='searchajax'),
    path('search_ajax2/', search_ajax2, name='searchajax2'),

    # testing dependant dropdowns
    path('searchbystate/', state_search, name='searchbystate'),
    path('searchstate_ajax/', searchstate_ajax, name='searchstateajax'),

    #path("state_name", state_name, name ='statename'),
    path("check-eval", check_evaluation, name='check_eval'),
    path("check-post-eval/<int:check_eval_id>/", check_post_evaluation, name='check_post'),

    # approver resources
    path('approver-list/', ApproverListView.as_view(), name='approver_home'),
    path('approver/<int:pk>/', ApproverDetailView.as_view(), name='approver_detail'),
    path('approver-create', ApproverCreateView.as_view(), name='approver_new'),
    path('approver-update/<int:pk>/', ApproverUpdateView.as_view(), name='approver_update'),
    path('approver-delete/<int:pk>/', ApproverDeleteView.as_view(), name='approver_delete'),

    # school resources
    path('school-list/', SchoolListView.as_view(), name='school_home'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('school-create', SchoolCreateView.as_view(), name='school_new'),
    path('school-update/<int:pk>/', SchoolUpdateView.as_view(), name='school_update'),
    path('school-delete/<int:pk>/', SchoolDeleteView.as_view(), name='school_delete'),
    path('school-search/', SchoolSearchView.as_view(), name='school_search'),

    # major resources
    path('major-list/', MajorListView.as_view(), name='major_home'),
    path('major-update/<int:pk>/', major_update, name='major_update'),
    path('major-delete/<int:pk>/', major_delete, name='major_delete'),
    path('major/<int:pk>/', MajorDetailView.as_view(), name='major_detail'),
    path('major-create', MajorCreateView.as_view(), name='major_new'),
    path('major-search', MajorSearchView.as_view(), name='major_search'),

    # course resources
    path('course-list/', CourseListView.as_view(), name='course_home'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course-create', CourseCreateView.as_view(), name='course_new'),
    path('course-update/<int:pk>/', CourseUpdateView.as_view(), name='course_update'),
    path('course-delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),


    # transfer evaluation
    path('transfereval/<int:pk>/', TransferEvaluationDetailView.as_view(), name='transfereval_detail'),
    path('transfereval-list/', TransferEvaluationListView.as_view(), name='transfereval_home'),
    path('transfereval-update/<int:pk>/', TransferEvaluationUpdateView.as_view(), name='transfereval_update'),
    path('transfereval-delete/<int:pk>/', TransferEvaluationDeleteView.as_view(), name='transfereval_delete'),
    path('transfereval-create', TransferEvaluationCreateView.as_view(), name='transfereval_new'),

    # major_requirement resources
    path('major-requirement-list/', Major_requirementListView.as_view(), name='major_requirement_home'),
    path('major-requirement/<int:pk>/', Major_requirementDetailView.as_view(), name='major_requirement_detail'),
    path('major-requirement-create', Major_requirementCreateView.as_view(), name='major_requirement_new'),
    path('major-requirement-update/<int:pk>/', Major_requirementUpdateView.as_view(), name='major_requirement_update'),
    path('major-requirement-delete/<int:pk>/', Major_requirementDeleteView.as_view(), name='major_requirement_delete'),


    #path('list/', DropDownListView.as_view(), name='person_changelist'),
    #path('add/', DropDownCreateView.as_view(), name='person_add'),
    #path('adds/', dropdown, name='person_add'),
    #path('<int:pk>/', PersonUpdateView.as_view(), name='person_change'),
    #path('ajax/load-cities/', load_majors, name='ajax_load_majors'),
    #path('ajax/load-vanues/', views.load_vanues, name='ajax_load_vanues'),
]
