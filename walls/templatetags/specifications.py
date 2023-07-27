from django import template
from ..models import *

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.simple_tag
def get_src(img=None):
    return Walls.objects.all()[0].wall
    
@register.simple_tag
def get_src_with_id(id=None):
    return Walls.objects.filter(pk=id)[0].wall