from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView
from .models import *

# Create your views here.


def _get_form(request, formcls, prefix):
    data = request.Post if prefix in request.Post else None
    return formcls(data, prefix=prefix)


class TableListView(ListView):
    model = Table
    template_name = "table_list.html"


class TableCreateView(TemplateView):
    pk_url_kwarg = 'table_no'
    template_name = "table_create.html"
   
    def get(self, request, *args, **kwargs):
        return self.render_to_response({'table_form': TableForm(prefix='TableForm_prefix'), 'column_form': ColumnForm(prefix='ColumnForm_prefix')})
 
    def post(self, request, *args, **kwargs):
        table_form = _get_form(request, TableForm, 'TableForm_prefix')
        column_form = _get_form(request, ColumnForm, 'ColumnForm_prefix')

        if table_form.is_bound and table_form.is_valid() and column_form.is_bound and column_form.is_valid():
            table_instance = table_form.save()
            column_instance = column_form.save()
            table_instance.Columns.add(column_instance) # resolve many-to-one relationship
            column_instance.serial_no = table_instance.column_num # update column serial number
            table_instance.column_num = table_instance.column_num + 1 # update table column number for next column

        return self.render_to_response({'table_form':table_form, 'column_form':column_form})


class TableDetailView(DetailView):
    model = Table
    pk_url_kwarg = 'table_no'
    template_name =  "table_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TableDetailView, self).get_context_data(**kwargs)
        return context


class TableDeleteView(DeleteView):
    model = Table

class TableUpdateView(UpdateView):
    model = Item
    fields = [
        'title',
        'description',
    ]
    success_url = "/mytables/"
