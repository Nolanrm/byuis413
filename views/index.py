from catalog import models as cmod
from account import models as amod
from django.db import models
from django_mako_plus import view_function, jscontext
from FOMO import settings
import math

@view_function
def process_request(request, cat:cmod.Category=None, pnum:int=1):
    #getting the products
    if cat is not None:
        p1 = cmod.Product.objects.filter(category=cat)
    else:
        p1 = cmod.Product.objects.all()
    #total page count
    page_count = math.ceil(p1.count()/6)  
    #list of categories
    c1 = cmod.Category.objects.all()


    if cat is None:
        title = 'All Products'
        cat = request.dmp.urlparams[0]
        context = {
            'p1': p1,
            jscontext('page_count'): page_count,
            jscontext('pnum'): pnum,
            'c1':c1,
            jscontext('cat'): cat,
            'title':title,
        }
    else:
        title = cmod.Category.objects.get(id=cat.id)
        context = {
                'p1': p1,
                jscontext('page_count'): page_count,
                jscontext('pnum'): pnum,
                'c1':c1,
                jscontext('cat'): cat.id,
                'title':title,
                'all_cat':'All Products'
            }


    return request.dmp.render('index.html', context)



#the javascript will provide the correct url for this function
#catalog/index.products/cid/pnum
#index is the py file #products is the function
@view_function
def products(request, cat:cmod.Category=None, pnum:int=1):


    if cat is not None:
        p1 = cmod.Product.objects.filter(category=cat)
    else:
        p1 = cmod.Product.objects.all()
    #total page count
    page_count = math.ceil(p1.count()/6)  
    #list of categories
    c1 = cmod.Category.objects.all()
    
    if cat is None:
        qry = cmod.Product.objects.all()
    else:
        qry = cmod.Product.objects.filter(category=cat)


    qry_end = pnum*6
    qry_start = qry_end - 6

    qry = qry[qry_start:qry_end] # use math to calculate the correct page instead of hard coded
    #qry[0:6] is item 0,1,2,3,4,5
    if cat is None:
        title = 'All Products'
        cat = request.dmp.urlparams[0]
        context = {
            'p1': p1,
            jscontext('page_count'): page_count,
            jscontext('pnum'): pnum,
            'c1':c1,
            jscontext('cat'): cat,
            'qry':qry,
            'title':title,
        }
    else:
        title = cmod.Category.objects.get(id=cat.id)
        context = {
                'p1': p1,
                jscontext('page_count'): page_count,
                jscontext('pnum'): pnum,
                'c1':c1,
                jscontext('cat'): cat.id,
                'title':title,
                'all_cat':'All Products',
                'qry':qry,
            }

    return request.dmp.render("index.products.html", context)

    #index.products.html inherits from base.ajax.htm