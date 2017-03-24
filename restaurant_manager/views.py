from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import *


def menu_create(request):
    items = Item.objects.all()
    context = {'items': items}
    template = loader.get_template('menu_create.html')
    return HttpResponse(template.render(context,request))


def post_menu_create(request):
    # if request.method == 'POST':
    #     menu = Menu.objects.get(id=request.POST['id'])
    menu = Menu(name='',time='00:00:00')
    d = request.POST
    if d["name"]:
        menu.name = d["name"]
    if d["time"]:
        menu.time = d["time"]
    Menu.save(menu)
    if d.getlist('menu'):
        # menu.items.clear()
        for i in d.getlist('menu'):
            item = Item.objects.get(id=int(i))
            menu.items.add(item)
    Menu.save(menu)
    return redirect('menu')


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
    return HttpResponse(template.render(context, request))


def change_form(request, menu_id):
    menu_item = Menu.objects.get(id=menu_id)
    items = Item.objects.all()
    template = loader.get_template('menu_form.html')
    context = {'menu_item': menu_item, 'items': items}
    return HttpResponse(template.render(context, request))


def item_form(request, menu_id):
    item = Item.objects.get(id=menu_id)
    template = loader.get_template('item_form.html')
    context = {'item': item}
    return HttpResponse(template.render(context, request))


def menu_delete(request, menu_id):
    menu_item = Menu.objects.get(id=menu_id)
    menu_item.delete()
    return HttpResponseRedirect('/menu/')


def item_delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect('/item/')


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
            menu.save()
            return redirect('menu')
