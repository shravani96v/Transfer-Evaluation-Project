from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from ..models.model_major_requirement import Major_requirement
from django.urls import reverse_lazy


def form_valid(self, form):
    return self.render_to_response(self.get_context_data(form=form))


class Major_requirementListView(ListView):
    model = Major_requirement
    template_name = 'major_requirement_html/major_requirement_home.html'


class Major_requirementDetailView(DetailView):
    model = Major_requirement
    template_name = 'major_requirement_html/major_requirement_detail.html'


class Major_requirementCreateView(CreateView):
    model = Major_requirement
    template_name = 'major_requirement_html/major_requirement_new.html'
    fields = ['description']
    success_url = reverse_lazy('major_requirement_home')


class Major_requirementUpdateView(UpdateView):
    model = Major_requirement
    template_name = 'major_requirement_html/major_requirement_update.html'
    fields = ['major_req_id', 'description']
    success_url = reverse_lazy('major_requirement_home')


class Major_requirementDeleteView(DeleteView):
    model = Major_requirement
    template_name = 'major_requirement_html/major_requirement_delete.html'
    success_url = reverse_lazy('major_requirement_home')
