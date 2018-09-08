from django.contrib import admin
from backend.models import *


class BaseGroupAdmin(admin.ModelAdmin):
    exclude = ('group', )

    def get_queryset(self, request):
        queryset = super(BaseGroupAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            group = request.user.groups.first()
            queryset = queryset.filter(group=group)
        return queryset

    def save_model(self, request, obj, form, change):
        obj.group = request.user.groups.first()
        super().save_model(request, obj, form, change)


class CustomerAdmin(BaseGroupAdmin):
    pass


class ContractAdmin(BaseGroupAdmin):
    pass


class AddressAdmin(BaseGroupAdmin):
    pass


class StreetTypeAdmin(BaseGroupAdmin):
    pass


class ServiceAdmin(BaseGroupAdmin):
    pass


class ServiceTypeAdmin(BaseGroupAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Contract, ContractAdmin)

admin.site.register(Address, AddressAdmin)
admin.site.register(StreetType, StreetTypeAdmin)

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
