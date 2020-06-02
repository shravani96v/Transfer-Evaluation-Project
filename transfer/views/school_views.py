from django.shortcuts import render   # redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from ..models.model_school import School
from django.urls import reverse_lazy
from django.db.models import Q


class HomeListView(ListView):
    model = School
    template_name = 'home.html'


class SchoolListView(ListView):
    # lists of all the object of model School
    model = School
    template_name = 'school_html/school_home.html'


class SchoolDetailView(DetailView):
    # detail view of all the object of model School
    model = School
    template_name = 'school_html/school_detail.html'


class SchoolCreateView(CreateView):
    # create view of all the object of model School
    model = School
    template_name = 'school_html/school_new.html'
    fields = ['school_id', 'school_name', 'state_name']
    success_url = reverse_lazy('school_home')


class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school_html/school_update.html'
    fields = ['school_id', 'school_name', 'state_name']
    success_url = reverse_lazy('school_home')


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school_html/school_delete.html'
    success_url = reverse_lazy('school_home')


class SchoolSearchView(ListView):
    # lists of all the object of model School
    model = School
    template_name = 'school_html/school_home.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = School.objects.filter(Q(school_name__icontains=query) | Q(state_name__icontains=query))
        return object_list
