from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:price_param>', views.get_price_by_num),
    path('<str:price_param>', views.get_price),
]
