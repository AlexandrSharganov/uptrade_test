from django.shortcuts import render

from .models import Menu

def index(request, pk=None):
    template = 'menu/index.html'
    menu = Menu.objects.all()
    if pk == None:
        context = {
            'menu' : menu,
        }
        return render(request, template, context)
    else:
        menu = Menu.objects.prefetch_related('items', 'submenu').get(pk=pk)
        context = {
            'menu' : menu,
            'pk': pk,
        }
        return render(request, template, context)


def index_second(request, pk=None):
    menu = Menu.objects.prefetch_related('items', 'submenu').all()
    template = 'menu/index_second.html'
    if pk == None:
        context = {
            'menu': menu,
        }
        return render(request, template, context)
    else:
        context = {
            'menu': menu,
            'pk': pk,
        }        
        return render(request, template, context)