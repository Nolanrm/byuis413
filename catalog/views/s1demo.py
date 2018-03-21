from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from formlib import Formless
from django import forms
from django.contrib.auth import authenticate, login
from account import models as amod

@view_function
def process_request(request):



    # render the template
    return request.dmp.render('s1demo.html')

