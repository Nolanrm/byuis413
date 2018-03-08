from django.contrib import admin
from catalog import models as cmod


admin.site.register(cmod.BulkProduct)
admin.site.register(cmod.Category)
admin.site.register(cmod.IndividualProduct)
admin.site.register(cmod.RentalProduct)