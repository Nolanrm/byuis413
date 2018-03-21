from catalog import models as cmod
#product_ids = session.getattr
# request.session.getattr
# product_ids
# product_ids
# request.lastfive

# convert request.last_five
# set the list of ids in tot he session

class LastfiveMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        mylist = request.session.get('lastfive')

        request.lastfive = []      
        
        for pid in mylist:
            request.lastfive.append(cmod.Product.objects.get(id = pid))       


        response = self.get_response(request)


        while(len(request.lastfive) >= 6):
            request.lastfive.pop()

        lastfive_ids = []

        for product in request.lastfive[0:6]:
            lastfive_ids.append(product.id)

        request.session['lastfive'] = lastfive_ids
  
        # Code to be executed for each request/response after
        # the view is called.

        return response