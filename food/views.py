from django.forms.models import BaseModelForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from food.models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     items = Item.objects.all()
    
#     context = {
#         'items':items,
#     }
#     return render(request, 'food\index.html', context )

class ItemListView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'


def item(request):

    return HttpResponse("<h1>its empty in here </h1>")

class ItemDetailView(DetailView):
    model = Item
    template_name = 'food/details.html'
    context_object_name = 'item'

# def details(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/details.html', context)
    

    
class ItemCreateView(CreateView):
    model = Item
    template_name = 'food/item-form.html'
    fields = ['name', 'desc', 'price', 'image']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


# def create_item(request):
#     #view for creating an item url name (create-item)
#     form = ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
    
#     return render(request, 'food/item-form.html', {'form': form})

@login_required
def edit_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if(item.user != request.user):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()

    if form.is_valid():
        if(item.user == request.user):
            form.save()
            return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})


def delete_item(request,id):

    item = Item.objects.get(id=id)
    if(item.user != request.user):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden()
    
    if request.method == 'POST':
        if(item.user == request.user):
            item.delete()
            return redirect('food:index')
 


    
    return render(request, 'food/delete-item.html', {'item': item})