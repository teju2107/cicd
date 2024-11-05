from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/new/', views.create_or_edit_item, name='item_create'),
    path('item/<int:id>/edit/', views.create_or_edit_item, name='item_edit'),
    path('item/<int:id>/delete/', views.delete_item, name='item_delete'),
]


