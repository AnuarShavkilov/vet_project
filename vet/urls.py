from django.urls import path, include
from . import views

urlpatterns = [
    path('<price_param>', views.get_price),
]
