from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

from .form import TestForm
from .models import DataSet
from .tasks import test_func


class AddView(FormView):
    template_name = 'add.html'
    form_class = TestForm
    success_url = '/'

    def form_valid(self, form):
        data_set = DataSet(a=form.cleaned_data.get('a'),
                           b=form.cleaned_data.get('b'))
        data_set.save()
        return super().form_valid(form)


class DataSetListView(ListView):
    template_name = 'dataset_list.html'
    model = DataSet


class ControlView(TemplateView):
    template_name = 'control.html'

    def post(self, request):
        data_sets = DataSet.objects.all()
        for data_set in data_sets:
            test_func.delay(data_set.id)
        return redirect('control_view')
