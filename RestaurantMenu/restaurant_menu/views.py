from django.shortcuts import render
from django.views import generic
from .models import MenuItem, MEAL_TYPE


# Create your views here.
class MenuList(generic.ListView):
    queryset = MenuItem.objects.order_by('date_created')
    template_name = 'menu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = MenuItem
    template_name = 'menu_item_detail.html'
