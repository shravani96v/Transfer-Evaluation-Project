from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from ..models.model_transfer_course import TransferCourse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import ModelForm


class CourseForm(ModelForm):
    class Meta:
        model = TransferCourse
        fields = ['transfer_course_id', 'school_id', 'subject_number', 'title']


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
    course = get_object_or_404(Course, pk=pk)
    return render(request, template_name, {'object': course})


def course_update(request, pk, template_name='course_html/course_update.html'):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_home')
    return render(request, template_name, {'form': form})


def course_delete(request, pk, template_name='course_html/course_delete.html'):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_home')
    return render(request, template_name, {'object': course})
