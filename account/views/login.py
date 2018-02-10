from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from formlib import Formless
from django import forms
from django.contrib.auth import authenticate, login
from account import models as amod

@view_function
def process_request(request):

    # process the form
    form = LoginForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/account/index/')

    # render the template
    return request.dmp_render('login.html', {
        'form': form,
    })


class LoginForm(Formless):   # extending formlib.Form, not Django's forms.Form
    '''An example form'''
    def init(self):
        '''Adds the fields for this form (called at end of __init__)'''
        self.fields['email'] = forms.CharField(label='Email Address')
        self.fields['password'] = forms.CharField(label='Password', widget =forms.PasswordInput())
        self.user = None

    def clean(self):
        UserEmail= self.cleaned_data.get('email')
        UserPassword=self.cleaned_data.get('password')
        
        print(UserEmail, UserPassword)
        self.user = authenticate(username = UserEmail ,password = UserPassword)
        if self.user is None:
            raise forms.ValidationError('Invalid Password')
        # ...
        return self.cleaned_data

    def commit(self):
        '''Process the form action'''
        login(self.request, self.user)
        # do something with c (optional)
       
        # act on the form
        print('>>>> Name is', self.cleaned_data['email'])
        # return any data (optional)
        return self.cleaned_data