from django.contrib import admin
from django.urls import path
from .views.major_requirement_views import *
from .views.course_views import *
from .views.major_views import *
from .views.school_views import *
from .views.transfer_evaluation_views import *
from .views.remove_data import *
from .views.approver_views import *
from .views.load import *
from .views.major_requirement_views import *
from .views.home import *

urlpatterns = [
    path('load-data/', import_file, name='import'),
    path('remove-data/', remove_all_data, name='remove_data'),
    path('', HomeListView.as_view(), name='home'),
    #path('result/',result),
    #approver resources
    path('approver-list/', ApproverListView.as_view(), name='approver_home'),
    path('approver/<int:pk>/', ApproverDetailView.as_view(), name='approver_detail'),
    path('approver-create', ApproverCreateView.as_view(), name='approver_new'),
    path('approver-update/<int:pk>/', ApproverUpdateView.as_view(), name='approver_update'),
    path('approver-delete/<int:pk>/', ApproverDeleteView.as_view(), name='approver_delete'),
    #school resources
    path('school-list/', SchoolListView.as_view(), name='school_home'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('school-create', SchoolCreateView.as_view(), name='school_new'),
    path('school-update/<int:pk>/', SchoolUpdateView.as_view(), name='school_update'),
    path('school-delete/<int:pk>/', SchoolDeleteView.as_view(), name='school_delete'),
    path('school-search', SchoolSearchView.as_view(), name='school_search'),

    #major resources
    path('major-list/', MajorListView.as_view(), name='major_home'),
    path('major-update/<int:pk>/', major_update, name='major_update'),
    path('major-delete/<int:pk>/', major_delete, name='major_delete'),
    path('major/<int:pk>/', MajorDetailView.as_view(), name='major_detail'),
    path('major-create', MajorCreateView.as_view(), name='major_new'),
    path('major-search', MajorSearchView.as_view(), name='major_search'),
    #course resources
    path('course-list/', course_list, name='course_home'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course-update/<int:pk>/', course_update, name='course_update'),
    path('course-delete/<int:pk>/', course_delete, name='course_delete'),
    path('course-create', course_create, name='course_new'),

    #### transfer evaluation
    path('transfereval-list/', TransferEvaluationListView.as_view(), name='transfereval_home'),
    path('transfereval/<int:pk>/', TransferEvaluationDetailView.as_view(), name='transfereval_detail'),
    path('transfereval-update/<int:pk>/', TransferEvaluationUpdateView.as_view(), name='transfereval_update'),
    path('transfereval-delete/<int:pk>/', TransferEvaluationDeleteView.as_view(), name='transfereval_delete'),
    path('transfereval-create', TransferEvaluationCreateView.as_view(), name='transfereval_new'),

    #major_requirement resources
    path('major-requirement-list/', Major_requirementListView.as_view(), name='major_requirement_home'),
    path('major-requirement/<int:pk>/', Major_requirementDetailView.as_view(), name='major_requirement_detail'),
    path('major-requirement-create', Major_requirementCreateView.as_view(), name='major_requirement_new'),
    path('major-requirement-update/<int:pk>/', Major_requirementUpdateView.as_view(), name='major_requirement_update'),
    path('major-requirement-delete/<int:pk>/', Major_requirementDeleteView.as_view(), name='major_requirement_delete'),
]
