from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from ..models.model_approver import Approver
from django.urls import reverse_lazy


class ApproverListView(ListView):
    # detail view of the object of model Major
    paginate_by = 5
    model = Approver
    template_name = 'approver_html/approver_home.html'


class ApproverDetailView(DetailView):
    # detail view of all the object of model approver
    model = Approver
    template_name = 'approver_html/approver_detail.html'


class ApproverCreateView(CreateView):
    # creates object in model Major
    model = Approver
    template_name = 'approver_html/approver_new.html'
    fields = ['approver_name']
    success_url = reverse_lazy('approver_home')


class ApproverUpdateView(UpdateView):
    model = Approver
    template_name = 'approver_html/approver_update.html'
    fields = ['approver_name']
    success_url = reverse_lazy('approver_home')


class ApproverDeleteView(DeleteView):
    model = Approver
    template_name = 'approver_html/approver_delete.html'
    success_url = reverse_lazy('approver_home')
