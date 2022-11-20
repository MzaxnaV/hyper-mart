from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='dashboard-index') ,
    path('brand/', views.brand, name='dashboard-brand'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),

    path('list/', views.list_items, name='list'),
    path('<int:product_id>/', views.detail, name='detail'),
]