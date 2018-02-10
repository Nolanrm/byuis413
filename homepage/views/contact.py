
## How to render the post from the form on contact?????
from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):

    if request.method == 'POST':
        print(request.POST['firstname'])
        print(request.POST['lastname'])
    context = {
    }

    return request.dmp_render('contact.html', context)
