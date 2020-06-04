from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from ..models.model_transferevaluation import Transferevaluation
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import ModelForm


class TransferevaluationForm(ModelForm):
    class Meta:
        model = Transferevaluation
        fields = ['course_id', 'major_req_id', 'sem_year_taken', 'expiration_date', 'approved_status', 'comment',  'approver_id']


class TransferEvaluationListView(ListView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_home.html'


class TransferEvaluationDetailView(DetailView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_detail.html'


class TransferEvaluationCreateView(CreateView):

    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_new.html'
    fields = ['transfer_eval_id']


class TransferEvaluationUpdateView(UpdateView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_update.html'
    fields = ['transfer_eval_id']


class TransferEvaluationDeleteView(DeleteView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_delete.html'
    success_url = reverse_lazy('transfer_eval_id')
