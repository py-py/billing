from decimal import Decimal
from backend.settings import VAT
__all__ = ('calculate_price_without_vat', 'calculate_vat', )


def calculate_vat(price):
    amount_vat = Decimal(100 / VAT)
    return Decimal((price / (amount_vat + 1)) * amount_vat).quantize(Decimal('1.00'))


def calculate_price_without_vat(price):
    amount_vat = Decimal(100 / VAT)
    return Decimal(price / (amount_vat + 1)).quantize(Decimal('1.00'))
