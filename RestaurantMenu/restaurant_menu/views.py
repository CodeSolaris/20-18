from django.shortcuts import render
from django.views import generic
from .models import MenuItem


# Create your views here.
class MenuList(generic.ListView):
    queryset = MenuItem.objects.order_by('date_created')
    template_name = 'menu_list.html'


class MenuItemDetail(generic.DetailView):
    model = MenuItem
    template_name = 'menu_item_detail.html'
