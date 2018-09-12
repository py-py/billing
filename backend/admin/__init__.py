from backend.models import *
from project.admin import invoice_admin
from .contract_admin import ContractAdmin


invoice_admin.register(Contract, ContractAdmin)

invoice_admin.register(Address)
invoice_admin.register(StreetType)

invoice_admin.register(Service)
invoice_admin.register(ServiceType)

invoice_admin.register(Company)
invoice_admin.register(LegacyEntity)
