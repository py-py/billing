from django.contrib import admin
from backend.models import *

# Register your models here.


admin.site.register(Customer)
admin.site.register(Contract)


admin.site.register(Address)
admin.site.register(StreetType)

admin.site.register(Service)
admin.site.register(ServiceType)
