from django.shortcuts import redirect, render
from django.http import HttpResponse
from food.models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.

def index(request):
    items = Item.objects.all()
    
    context = {
        'items':items,
    }
    return render(request, 'food\index.html', context )

def item(request):

    return HttpResponse("<h1>its empty in here </h1>")

def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/details.html', context)

def create_item(request):
    #view for creating an item url name (create-item)
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form})

def edit_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})

def delete_item(request,id):

    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/delete-item.html', {'item': item})