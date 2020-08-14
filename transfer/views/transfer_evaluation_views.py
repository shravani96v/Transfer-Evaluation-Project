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
        fields = ['transfer_course_id', 'major_req_id', 'sem_year_taken', 'expiration_date', 'approved_status', 'notes',  'approver_id']


class TransferEvaluationListView(ListView):
    paginate_by = 5
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_home.html'


class TransferEvaluationDetailView(DetailView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_detail.html'
    #success_url = reverse_lazy('transfereval_home')


class TransferEvaluationCreateView(CreateView):

    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_new.html'
    fields = ['transfer_eval_id']


class TransferEvaluationUpdateView(UpdateView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_update.html'
    fields = ['transfer_course_id', 'major_req_id', 'sem_year_taken', 'expiration_date', 'approved_status', 'notes']
    success_url = reverse_lazy('transfereval_home')
    context_object_name = 'object_list'

#def TransferEvaluationUpdateView(request, pk, template_name='transferevaluation_html/transfereval_update.html'):
#    transfereval = get_object_or_404(Transferevaluation, pk=pk)
#    form = TransferevaluationForm(request.POST or None, instance=transfereval)
#    if form.is_valid():
#        form.save()
#        return redirect('transfereval_home')
#    return render(request, template_name, {'object': object})


class TransferEvaluationDeleteView(DeleteView):
    model = Transferevaluation
    template_name = 'transferevaluation_html/transfereval_delete.html'
    success_url = reverse_lazy('home')
