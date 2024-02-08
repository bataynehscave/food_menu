from django.urls import path
from . import views

app_name="food"
urlpatterns = [
    #shows all items
    path('', views.index, name='index'),
    #empty path
    path('item', views.item, name='item-view'),
    #shows individual items
    path('item/<int:item_id>', views.details, name='item-details'),
    #add item
    path('create_item', views.create_item, name='create-item'),
    #edit item
    path('edit_item/<int:id>', views.edit_item, name='edit-item'),
    #delete item
    path('delete_item/<int:id>', views.delete_item, name='delete-item')
]