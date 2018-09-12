# Created by ruslan_valeev at 9/12/18
from backend.admin.base_admin import BaseGroupAdmin

__all__ = ('CompanyAdmin', 'LegacyEntityAdmin', )


class CompanyAdmin(BaseGroupAdmin):
    pass


class LegacyEntityAdmin(BaseGroupAdmin):
    pass
