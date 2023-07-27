from django.shortcuts import render
from walls.models import *
from django.views.generic import DetailView

# Create your views here.

def home(request):
    items = Walls.objects.all()
    data={
        "items": items,
        "cat_selected": 'all'
    }
    return render(request, 'home/home.html', data)



def home_filters(request, catID, sort):
    if catID == 0:
        items = Walls.objects.order_by(sort)
    else:
        items = Walls.objects.order_by(sort).filter(cat = catID)



    catList = Category.objects.all()
    sortList = ["Дате", "Популярности"]


    data={
        "items": items,
        "cat_selected": 'filters',
        'catList': catList,
        "sortList": sortList,
    }
   
    return render(request, 'home/home-filters.html', data)




def home_recomendations(request):
    items = Walls.objects.filter(cat = 24)
    data={
        "items": items,
        "cat_selected": 'recomendations'
    }
    return render(request, 'home/home.html', data)





class Content(DetailView):
    model = Walls
    template_name = 'home/post.html'
    context_object_name = 'item'

    
