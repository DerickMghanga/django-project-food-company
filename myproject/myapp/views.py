from django.shortcuts import render

from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')
    

def menu_by_id(request):
    new_menus =  Menu.objects.all()
    newmenu_dict = {'menu': new_menus}
    return render(request, 'menu_cards.html', newmenu_dict)