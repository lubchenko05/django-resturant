from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import *


def item_list(request):
    items = Item.objects.order_by('name')
    template = loader.get_template('item_list.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context,request))

def menu_list(request):
    menu_list = Menu.objects.order_by('name')
    template = loader.get_template('menu_list.html')
    context = {
        'menu_list':menu_list
    }
    return HttpResponse(template.render(context,request))


def change_form(request, menu_id):
    menu_item = Menu.objects.get(name=menu_id.lower())
    items = Item.objects.all()
    template = loader.get_template('menu_form.html')
    context = {'menu_item': menu_item, 'items': items}
    return HttpResponse(template.render(context, request))


def menu_delete(request, menu_id):
    menu_item = Menu.objects.get(name=menu_id.lower())
    menu_item.delete()
    return HttpResponseRedirect('/menu/')


def post_change_form(request):
        if request.method == 'POST':
            menu = Menu.objects.get(id=request.POST['id'])
        d = request.POST
        if d["name"]:
            menu.name = d["name"]
        if d["time"]:
            menu.time = d["time"]
        if d.getlist('menu'):
            menu.items.clear()
            for i in d.getlist('menu'):
                item = Item.objects.get(id=int(i))
                menu.items.add(item)
        return redirect('menu')
