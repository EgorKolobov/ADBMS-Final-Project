from django.contrib import admin
from django.urls import path
from .views import (
    home,
    SupplierListView,
    SupplierDetailView,
    SupplierCreateView,
    SupplierDeleteView,
    SuppliersUpdateView
)

urlpatterns = [
    path('', home, name='adbms-home'),
    path('suppliers/', SupplierListView.as_view(), name='suppliers'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/new/', SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
    path('suppliers/<int:pk>/update/', SuppliersUpdateView.as_view(), name='supplier-update'),
    path('admin/', admin.site.urls),
]
