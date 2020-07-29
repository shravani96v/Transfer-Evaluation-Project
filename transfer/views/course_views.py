from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from ..models.model_transfer_course import TransferCourse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import ModelForm


class CourseCreateView(CreateView):
    # create view of all the object of model School
    model = TransferCourse
    template_name = 'course_html/course_new.html'
    fields = ['school_id', 'subject_number', 'title']
    success_url = reverse_lazy('course_home')


class CourseListView(ListView):
    # lists of all the object of model TransferCourse
    model = TransferCourse
    template_name = 'course_html/course_home.html'


class CourseDetailView(DetailView):
    # detail view of all the object of model TransferCourse
    model = TransferCourse
    template_name = 'course_html/course_detail.html'


class CourseUpdateView(UpdateView):
    model = TransferCourse
    template_name = 'course_html/course_update.html'
    fields = ['school_id', 'subject_number', 'title']
    success_url = reverse_lazy('course_home')


class CourseDeleteView(DeleteView):
    model = TransferCourse
    template_name = 'course_html/course_delete.html'
    success_url = reverse_lazy('course_home')


"""
def course_list(request, template_name='course_html/course_home.html'):
    course = TransferCourse.objects.all()
    data = {}
    data['object_list'] = course
    return render(request, template_name, data)

def course_create(request, template_name='course_html/course_new.html'):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_hom66e')
    return render(request, template_name, {'form': form})


def course_detail(request, pk, template_name='course_html/course_detail.html'):
    course = get_object_or_404(TranserCourse, pk=pk)
    return render(request, template_name, {'object': course})

class CourseDetailView(DetailView):
    # detail view of all the object of model School
    model = TransferCourse
    template_name = 'course_html/course_detail.html'

class CourseUpdateView(UpdateView):
    model = TransferCourse
    template_name = 'course_html/course_update.html'
    fields = ['subject_number', 'title']
    success_url = reverse_lazy('course_home')

def course_update(request, pk, template_name='course_html/course_update.html'):
    course = get_object_or_404(TranserCourse, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_home')
    return render(request, template_name, {'form': form})


def course_delete(request, pk, template_name='course_html/course_delete.html'):
    course = get_object_or_404(TransferCourse, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_home')
    return render(request, template_name, {'object': course})
"""
