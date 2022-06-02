from django.contrib import admin
from django.urls import path
from django.urls import include
from.import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('supplies_code/',views.index, name='supplies_code'),
    path("labor_code/", views.showLaborCode, name="show_labor_code"),
    path("new_labor/", views.AddNewLaborUsingModelForm.as_view(), name="add_new_labor"),
    path("labor_code/update_labor/<str:labor_class>", views.update_labor, name="update_labor"),
    path("labor_code/update_labor/updaterecord/<str:labor_class>", views.updaterecord, name='updaterecord' ),
    # path('update_labor/',views.update_labor, name='update_labor'),

    path("supply_code/", views.showSupplyCode, name="show_supply_code"),
    path("new_supply/", views.AddNewSupplyUsingModelForm.as_view(), name="add_new_supply"),
]