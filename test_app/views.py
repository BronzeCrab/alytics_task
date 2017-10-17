from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .form import TestForm
from .models import DataSet


class TestView(FormView):
    template_name = 'test.html'
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
