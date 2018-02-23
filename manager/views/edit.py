from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from formlib import Formless
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    #pulling id from url, given from the catalog/productlist.html page
    p1 = cmod.Product.objects.get(id=request.urlparams[0])
    if p1.__class__.__name__ == 'BulkProduct':
        form = EditForm(request, initial= {
            'TYPE_CHOICES': 1,
            'name' : p1.name,
            'description':p1.description,
            'status': p1.status,
            'category': p1.category,
            'price': p1.price,
            'quantity': p1.quantity,
            'reorder_quantity':p1.reorder_quantity,
            'reorder_trigger':p1.reorder_trigger,
        })
       

    elif p1.__class__.__name__=='IndividualProduct':
        form = EditForm(request, initial= {
            'TYPE_CHOICES': 2,
            'name' : p1.name,
            'description':p1.description,
            'status': p1.status,
            'category': p1.category,
            'price': p1.price,
            'pid': p1.pid,
        })
    elif p1.__class__.__name__=='RentalProduct':
        form = EditForm(request, initial= {
            'TYPE_CHOICES': 3,
            'name' : p1.name,
            'description':p1.description,
            'status': p1.status,
            'category': p1.category,
            'price': p1.price,
            'pid': p1.pid,
            'max_rental_days':p1.max_rental_days,
            'retire_date':p1.retire_date
        })

    if form.is_valid():
        
        
        form.commit(request)

        return HttpResponseRedirect('/catalog/productlist')
        #commit 
        #return to productlist

    product = {
        'product': p1,
        'form':form,
    }

    return request.dmp_render('edit.html', product)

class EditForm(Formless):
    
    def init(self):

        qs = cmod.Category.objects.all()

        self.fields['TYPE_CHOICES'] = forms.ChoiceField(choices=[ ['1', 'Bulk'], ['2','Individual'],['3','Rental'] ], required=False)
        self.fields['name'] = forms.CharField(label='Product Name', required=False)
        self.fields['description'] = forms.CharField(label='Description',  required=False)
        self.fields['category'] = forms.ModelChoiceField(queryset=qs,  required=False)
        self.fields['status'] = forms.ChoiceField(choices=[ ['A','A' ],['I','I'] ],  required=False)
        self.fields['price'] = forms.DecimalField(max_digits=7,decimal_places=2,  required=False)
        #BulkProduct
        self.fields['quantity'] = forms.IntegerField(label='Quantity',  required=False)
        self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger', required=False)
        self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity', required=False)
        #IndividualProduct And Rental
        self.fields['pid'] = forms.CharField(label='PID', required=False)
        #RentalProduct
        self.fields['max_rental_days'] = forms.IntegerField(label='Max Rental Days', required=False)
        self.fields['retire_date'] =forms.DateField(label='Retire Date', required=False)

    def clean_name(self):
            if self.cleaned_data.get('name') == '':
                raise forms.ValidationError('Name field is required')
            return self.cleaned_data.get('name')

    def clean_description(self):
        if self.cleaned_data.get('description') == '':
            raise forms.ValidationError('Description is required')
        return self.cleaned_data.get('description')
    
    def clean_category(self):
        if self.cleaned_data.get('category') is None:
            raise forms.ValidationError('Category is required')
        return self.cleaned_data.get('category')

    def clean_price(self):
        if self.cleaned_data.get('price') is None:
            raise forms.ValidationError('Price is required')
        return self.cleaned_data.get('price')
    
    def clean(self):

        #checked if a Bulk product is being created
        if self.cleaned_data.get('TYPE_CHOICES') == '1':
            if self.cleaned_data.get('quantity') is None:

                raise forms.ValidationError('Quantity is Required for Bulk Products')

            if self.cleaned_data.get('reorder_quantity') is None:
                raise forms.ValidationError('Reorder Quantity is Required for Bulk Products')

            if self.cleaned_data.get('reorder_trigger') is None:
                raise forms.ValidationError('Reorder Trigger is required for Bulk Products')

        #check pid if an individual products is being created
        elif self.cleaned_data.get('TYPE_CHOICES') == '2':
            if self.cleaned_data.get('pid') == '':
                raise forms.ValidationError('pid is required for this product')

        #check if a rental product is being created
        elif self.cleaned_data.get('TYPE_CHOICES') == '3':
            if self.cleaned_data.get('pid') == '':
                raise forms.ValidationError('pid is required for this product')
            if self.cleaned_data.get('max_rental_days') is None:
                raise forms.ValidationError('Max rental days is required for Rental Products')

            #Retire Date is not a required field

        return self.cleaned_data


    def commit(self, request):

        if self.cleaned_data.get('TYPE_CHOICES') == '1':
            p1 = cmod.Product.objects.get(id=request.urlparams[0])  

            p1.status = self.cleaned_data.get('status')
            p1.name = self.cleaned_data.get('name')
            p1.description = self.cleaned_data.get('description')
            p1.category = self.cleaned_data.get('category')
            p1.price = self.cleaned_data.get('price')

            p1.reorder_quantity = self.cleaned_data.get('reorder_quantity')
            p1.reorder_trigger = self.cleaned_data.get('reorder_trigger')
            p1.quantity = self.cleaned_data.get('quantity')
            
            p1.save()

        elif self.cleaned_data.get('TYPE_CHOICES') == '2':
            p1 = cmod.Product.objects.get(id=request.urlparams[0])

            p1.status = self.cleaned_data.get('status')
            p1.name = self.cleaned_data.get('name')
            p1.description = self.cleaned_data.get('description')
            p1.category = self.cleaned_data.get('category')
            p1.price = self.cleaned_data.get('price')

            p1.pid = self.cleaned_data.get('pid')

            p1.save()
        
        elif self.cleaned_data.get('TYPE_CHOICES') == '3':
            p1 = cmod.Product.objects.get(id=request.urlparams[0])

            p1.status = self.cleaned_data.get('status')
            p1.name = self.cleaned_data.get('name')
            p1.description = self.cleaned_data.get('description')
            p1.category = self.cleaned_data.get('category')
            p1.price = self.cleaned_data.get('price')

            p1.pid = self.cleaned_data.get('pid')
            p1.max_rental_days = self.cleaned_data.get('max_rental_days')
            p1.retire_date = self.cleaned_data.get('retire_date')

            p1.save()
        else:
            pass

