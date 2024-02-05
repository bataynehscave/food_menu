from django.urls import path
from . import views

app_name="food"
urlpatterns = [
    path('', views.index, name='index'),
    path('item', views.item, name='item-view'),
    path('item/<int:item_id>', views.details, name='item-details')
]