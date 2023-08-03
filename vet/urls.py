from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_price, name = 'main'),
    path('type', views.index_type, name = 'types'),
    path('type/<str:price_type>', views.get_type, name='type-name'),
    path('<int:price_param>', views.get_price_by_num),
    path('<str:price_param>', views.get_price, name='price-name'),
]
