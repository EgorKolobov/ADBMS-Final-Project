from django.shortcuts import render, get_object_or_404
from .models import Supplier
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)


def home(request):
    return render(request, 'ADBMS/index.html', {'title': 'Home'})


class SupplierListView(ListView):
    model = Supplier
    template_name = 'ADBMS/suppliers.html'
    context_object_name = 'suppliers'
    extra_context = {'title': 'All Suppliers'}


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'ADBMS/supplier_detail.html'
    context_object_name = 'supplier'
    extra_context = {'title': 'Supplier\'s details'}


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "ADBMS/supplier_form.html"
    fields = ['name', 'shipment_postal_code', 'shipment_address']


class SupplierDeleteView(DeleteView):
    model = Supplier
    context_object_name = 'supplier'
    success_url = '/suppliers/'


class SuppliersUpdateView(UpdateView):
    model = Supplier
    template_name = "ADBMS/supplier_update_form.html"
    fields = ['name', 'shipment_postal_code', 'shipment_address']
    # success_url = '/suppliers/'
