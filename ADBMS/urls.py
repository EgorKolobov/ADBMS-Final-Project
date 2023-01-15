from django.contrib import admin
from django.urls import path
from .views import home, neo4j_query1

urlpatterns = [
    path('', home, name='adbms-home'),
    path('neo4j-query1/', neo4j_query1, name='neo4j-query1'),
    path('admin/', admin.site.urls),
]
