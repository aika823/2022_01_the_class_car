from django.urls import path, include
from car_app import views

urlpatterns = [
    path("admin/", include("admin.urls")),
    path('', views.index)
]
