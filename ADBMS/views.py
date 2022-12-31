from django.shortcuts import render, get_object_or_404
from .models import Supplier
from django.views.generic import (
    ListView,
    CreateView,
)


def home(request):
    return render(request, 'ADBMS/index.html', {'title': 'Home'})


class SupplierListView(ListView):
    model = Supplier
    template_name = 'ADBMS/suppliers.html'
    context_object_name = 'suppliers'
    extra_context = {'title': 'All Suppliers'}


# class SupplierDetailView(ListView):
#     model = Supplier
#     template_name = 'ADBMS/supplier_detail.html'
#     context_object_name = 'suppliers'
#     extra_context = {'title': 'Supplier\'s details'}
def supplier_detail_view(request, pk):
    context = {'supplier': Supplier.objects.get(pk=pk)}
    return render(request, 'ADBMS/supplier_detail.html', context)


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "ADBMS/supplier_form.html"
    fields = ['name', 'shipment_postal_code', 'shipment_address']
