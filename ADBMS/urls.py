from django.contrib import admin
from django.urls import path
from .views import home, neo4j_query1, neo4j_query2, neo4j_query3, neo4j_query4

urlpatterns = [
    path('', home, name='adbms-home'),
    path('neo4j-query1/', neo4j_query1, name='neo4j-query1'),
    path('neo4j-query2/', neo4j_query2, name='neo4j-query2'),
    path('neo4j-query3/', neo4j_query3, name='neo4j-query3'),
    path('neo4j-query4/', neo4j_query4, name='neo4j-query4'),
    path('admin/', admin.site.urls),
]
