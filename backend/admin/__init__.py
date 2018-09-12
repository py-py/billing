from backend.models import *
from project.admin import invoice_admin

from .address_admin import *
from .company_admin import *
from .contract_admin import *
from .service_admin import *


invoice_admin.register(Contract, ContractAdmin)

invoice_admin.register(Address, AddressAdmin)
invoice_admin.register(StreetType, StreetTypeAdmin)

invoice_admin.register(Service, ServiceAdmin)
invoice_admin.register(ServiceType, ServiceTypeAdmin)

invoice_admin.register(Company, CompanyAdmin)
invoice_admin.register(LegacyEntity, LegacyEntityAdmin)
