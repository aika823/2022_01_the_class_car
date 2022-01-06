from django.urls import path

from . import views

app_name = "admin"

urlpatterns = [
    path('', views.sell),

    path('login', views.login),
    path('logout', views.logout),
    
    path('sell', views.sell),
    path('sell/<int:id>', views.sell_detail),

    path('buy', views.buy),
    path('buy/<int:id>', views.buy_detail),

    path('installment', views.installment),
    path('installment/<int:id>', views.installment_detail),
    
    path('create', views.create),
    path('delete', views.delete)
]