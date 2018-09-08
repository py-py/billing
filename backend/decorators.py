from django.core.exceptions import PermissionDenied
from django.http import Http404

from backend.models import Contract


def contract_permission_required(function):
    def wrapper(request, *args, **kwargs):
        try:
            contract = Contract.objects.get(pk=kwargs['contract_id'])
            if request.user in contract.group.user_set.all():
                return function(request, *args, **kwargs)
        except Contract.DoesNotExist as e:
            raise Http404
        raise PermissionDenied
    return wrapper
