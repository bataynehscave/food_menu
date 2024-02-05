from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item
from django.template import loader
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