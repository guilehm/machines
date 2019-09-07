from django.urls import path
from machines.web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
]
