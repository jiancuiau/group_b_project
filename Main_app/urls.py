from django.contrib import admin
from django.urls import path
from django.urls import include
from.import views


urlpatterns = [
    path('', views.index, name='index'),
    path("labor_code/", views.showLaborCode, name="show_labor_code"),
    path("new_labor/", views.AddNewLaborUsingModelForm.as_view(), name="add_new_labor"),
]