from django.contrib import admin
from django.urls import path
from .views import (
    home,
    SupplierListView,
    # SupplierDetailView,
    supplier_detail_view,
    SupplierCreateView,
)

urlpatterns = [
    path('', home, name='adbms-home'),
    path('suppliers/', SupplierListView.as_view(), name='suppliers'),
    path('suppliers/<int:pk>/', supplier_detail_view, name='supplier-detail'),
    path('suppliers/new/', SupplierCreateView.as_view(), name='supplier-create'),
    path('admin/', admin.site.urls),
]
