from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from datetime import datetime, timezone
import math 

ITEMS_PER_PAGE = 8

@view_function
def process_request(request, page:int=1):
    #products = cmod.Product.objects.filter(status="A") ONLY ACTIVE
    drugs = cmod.Drug.objects.all() #all
    

    drugs = drugs[(page - 1) * ITEMS_PER_PAGE: page * ITEMS_PER_PAGE]
    

    context = {
        'drugs': drugs,
        'page': page,
        'numpages': math.ceil(drugs.count() / ITEMS_PER_PAGE),
    }

    return request.dmp.render('index.html', context)
    