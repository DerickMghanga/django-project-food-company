from django.shortcuts import render

from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    newmenu = {'mains': [
        {'name': 'falafel', 'price': '12'},
        {'name': 'gyro', 'price': '10'},
        {'name': 'shawarma', 'price': '15'},
        {'name': 'humus', 'price': '5'},
    ]}
    return render(request, 'menu.html', newmenu)
    

def menu_by_id(request):
    new_menus =  Menu.objects.all()
    newmenu_dict = {'menu': new_menus}
    return render(request, 'menu_cards.html', newmenu_dict)