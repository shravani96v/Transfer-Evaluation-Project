from django.views.generic import TemplateView, ListView
#from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
#from django.views.generic.edit import CreateView
#from django.http import HttpResponse
from ..models.model_transferevaluation import Transferevaluation
#from django.shortcuts import render, redirect, get_object_or_404
#from django.urls import reverse_lazy
#from django.forms import ModelFor

class Home(TemplateView):
    template_name = 'home.html'

class TransferEvaluationListViewHome(ListView):
    model = Transferevaluation
    template_name = 'home.html'
