from django.urls import path
from . import views


app_name = 'webapp'
urlpatterns = [
    path('', views.employeeList.as_view())
]