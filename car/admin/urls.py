from django.urls import path

from . import views

app_name = "admin"

urlpatterns = [
    path('', views.consulting),

    path('login', views.login),
    path('logout', views.logout),
    
    path('consulting', views.consulting),
    path('consulting/<int:id>', views.consulting_detail),
    
    path('create', views.create),
    path('delete', views.delete)
]