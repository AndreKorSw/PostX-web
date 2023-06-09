from django import template
from xforum.models import *
register=template.Library()



# @register.inclusion_tag("xforum/list_categories.html")
@register.inclusion_tag('xforum/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats=Category.objects.all()
    else:
        cats=Category.objects.order_by(sort)
    return {"cats":cats,"cat_selected":cat_selected}