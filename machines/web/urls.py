from django.urls import path
from machines.web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/<int:machine_id>/', views.machine_detail, name='machine-detail'),
    path('modules/<int:module_id>/', views.module_detail, name='module-detail'),
    path('variations/<int:variation_id>/', views.variation_detail, name='variation-detail'),
]
