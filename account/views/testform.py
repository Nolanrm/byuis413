from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    #process form
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            #once you get here, everything is clean don't do more data changes
            #you can no longer inform the user that we have a problem
            print(form.cleaned_data)
            #do the work of the form
            #make the payment
            #create the user
            return HttpResponseRedirect('/account/welcome/')
    else:
        form = TestForm()

    context = {
        'form':form,
    }

    return request.dmp.render('testform.html', context)

class TestForm(forms.Form):
    favorite_ice_cream = forms.CharField(label="Favorite Ice Cream")
    renewal_date = forms.DateField(label="Renewal",help_text="Enter right data.")
    age = forms.IntegerField(label='Age')


    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('you are not 18, no soup for you')
        return age + 100

    

