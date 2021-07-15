from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("products/", views.products, name='products'),
    path("order/<str:pk>/", views.order_list, name='order-list'),

    path('create-order/', views.createOrderForm, name='create-order'),
    path('update-order/<str:pk>/', views.updateOder, name='update-order'),
    path('delete-order/<str:pk>/', views.deleteOrder, name='delete-order')
]
