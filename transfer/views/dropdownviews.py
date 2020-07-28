from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from ..models.model_major import Major
from ..models.dropdown import DropDown
from ..forms import DropDownForm


class DropDownListView(ListView):
    model = DropDown
    template_name = 'dropdown_list.html'
    context_object_name = 'dropdown'


class DropDownCreateView(CreateView):
    model = DropDown
    template_name = 'dropdown_form.html'
    form_class = DropDownForm
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = DropDown
    form_class = DropDownForm
    success_url = reverse_lazy('person_changelist')

def load_majors(request):
    school_id = request.GET.get('school')
    majors = DropDown.objects.filter(school_id=school_id).order_by('school')
    context = {'majors': majors}
    return render(request, 'major_dropdown_list_options.html', context)


def dropdown(request):
    dropdown_form = DropDownForm()
    return render(request, "dropdown_form.html", {"dropdown_form": dropdown_form})
