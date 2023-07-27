import random
from unicodedata import name
from django.shortcuts import render
from .models import *

# Create your views here.
def walls(request):
    data = {
        'imgs': Walls.objects.all(),
        'range_top': range(4),
        'range_left': range(4, 6),
        'range_right': range(6, 8),
        'range_bottom': range(8, 12),
    }
    return render(request, 'walls/walls.html', data)



def compilation(request):
    lst = []
    w = Walls.objects

    if len(w.all()) >= 16:
        for wall in random.sample(list(w.all()), 16):
            lst.append(wall.id)
    else:
        lst = [w.all()[0].id for i in range(16)]

    data = {
        'all_walls': w,
        'random_id': lst
    }
    return render(request, 'walls/compilation.html', data)

