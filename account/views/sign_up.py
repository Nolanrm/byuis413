from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.contrib.auth import login, authenticate
from account import models as amod
from formlib import Formless
import re

@view_function
def process_request(request):
    #process form
    form = SignUpForm(request)
    if form.is_valid():
        form.commit()
            #once you get here, everything is clean don't do more data changes
            #you can no longer inform the user that we have a problem
            #do the work of the form
            #make the payment
            #create the user
        return HttpResponseRedirect('/account/index/')

    return request.dmp_render('sign_up.html', {'form':form,})

class SignUpForm(Formless):

    def init(self):
        self.fields['first_name'] = forms.CharField(label="First Name")
        self.fields['last_name'] = forms.CharField(label='Last Name')
        self.fields['email'] = forms.EmailField(label="Email")
        self.fields['password'] = forms.CharField(label="Password")#help_text="Incorrect Password"
        self.fields['password2'] = forms.CharField(label='Confirm Password')
        self.fields['address'] = forms.CharField(label='Address')
        self.fields['city'] = forms.CharField(label='City')
        self.fields['state'] = forms.CharField(label="State")
        self.fields['zipcode'] = forms.IntegerField(label="Zip Code")
        self.user = None

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')

        if p1 != p2:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data

    def clean_password(self):
        p1 = self.cleaned_data.get('password')
        
        x=True
        while x:
            if (len(p1)<7):
                raise forms.ValidationError('Password must contain at least 8 characters')
            elif not re.search("[a-z]",p1):
                raise forms.ValidationError('Password must contain a letter')
            elif not re.search("[0-9]",p1):
                raise forms.ValidationError('Password must contain a number')
            else:
                print("Valid Password")
                x=False
                break

        return p1

    def clean_email(self):
        if  amod.User.objects.filter(email=self.cleaned_data.get('email')).count() > 0:
            raise forms.ValidationError('This is not a unique email')

        print(self.cleaned_data.get('email'))
        print(self.cleaned_data.get('first_name'))

        return self.cleaned_data.get('email')
        
    def commit(self):
        User = amod.User()
        User.email = self.cleaned_data.get('email')
        User.set_password(self.cleaned_data.get('password'))
        User.first_name = self.cleaned_data.get('first_name')
        User.last_name = self.cleaned_data.get('last_name')
        User.address = self.cleaned_data.get('address')
        User.city = self.cleaned_data.get('city')
        User.state = self.cleaned_data.get('state')
        User.zipcode = self.cleaned_data.get('zipcode')

        User.save()
        
        self.user = authenticate(username = self.cleaned_data.get('email') ,password = self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Sign-up failed')

        login(self.request, User)



