from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
  path('', views.orders_list, name='orders_list'),
  path('new/', views.order_create, name='order_new'),
  path('edit/<int:pk>/', views.order_update, name='order_edit'),
  path('delete/<int:pk>/', views.order_delete, name='order_delete'),
  path('export/', views.export_orders, name='order_export'),
  path('stats/', views.order_stats, name='order_stats')
]