from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:price_param>', views.get_price_by_num),
    path('<str:price_param>', views.get_price, name='price-name'),
]
