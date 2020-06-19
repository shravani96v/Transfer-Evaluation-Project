from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from ..models.model_major import Major
from django.urls import reverse_lazy
from django.forms import ModelForm
from django.db.models import Q
from django.http import HttpResponse
from ..models.model_school import School


class MajorSearchViewer(ListView):
    # list view of the object of model Major
    model = Major
    template_name = 'viewer.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Major.objects.filter(Q(major_name__icontains=query))
        return object_list


class SchoolSearchViewer(ListView):
    # lists of all the object of model School
    model = School
    template_name = 'viewer.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = School.objects.filter(Q(school_name__icontains=query) | Q(state_name__icontains=query))
        return object_list
