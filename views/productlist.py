from catalog import models as cmod
from account import models as amod
from django.db import models
from django_mako_plus import view_function, jscontext


@view_function
def process_request(request):


    if request.dmp.urlparams[0] != '':
        #need to add try except incase an invalid number is put in the url
           p2 = cmod.Product.objects.get(id=request.dmp.urlparams[0])
           p2.status = 'I'
           p2.save()

    p1 = cmod.Product.objects.filter(status = 'A')
    
    products = {
            'p1': p1,
        }
    

    return request.dmp.render('productlist.html', products)