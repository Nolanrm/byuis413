from catalog import models as cmod
from account import models as amod
from django.db import models
from django_mako_plus import view_function, jscontext
from FOMO import settings
import math

@view_function
def process_request(request):
    #getting the products
    product = cmod.Product.objects.get(id=request.dmp.urlparams[0])

    if product in request.lastfive:
        request.lastfive.remove(product)
        request.lastfive.insert(0,product)   
    else:
        request.lastfive.insert(0,product)

    context = {
        'p': product,
    }

    return request.dmp.render('details.html', context)




