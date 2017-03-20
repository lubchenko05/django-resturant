from django.http import HttpResponse
from django.template import loader
from .models import *

def change_form(request, menu_id):
    menu_item = Menu.objects.get(id=menu_id)
    template = loader.get_template('menu_form.html')
    context = {
        'menu_item': menu_item,
    }
    return HttpResponse(template.render(context, request))
