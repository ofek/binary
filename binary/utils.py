from decimal import Decimal as _Decimal


class Decimal(_Decimal):
    def __new__(cls, value='0', context=None):
        if isinstance(value, float):
            value = str(value)
        return super(Decimal, cls).__new__(cls, value, context)

    def __add__(self, other, context=None):
        if isinstance(other, float):
            other = Decimal(other)
        return Decimal(super(Decimal, self).__add__(other))
    __radd__ = __add__

    def __sub__(self, other, context=None):
        if isinstance(other, float):
            other = Decimal(other)
        return Decimal(super(Decimal, self).__sub__(other))
    __rsub__ = __sub__

    def __mul__(self, other, context=None):
        if isinstance(other, float):
            other = Decimal(other)
        return Decimal(super(Decimal, self).__mul__(other))
    __rmul__ = __mul__

    def __truediv__(self, other, context=None):
        if isinstance(other, float):
            other = Decimal(other)
        return Decimal(super(Decimal, self).__truediv__(other))
    __rtruediv__ = __truediv__

    # TODO: remove when Python 2 EOL
    __div__ = __truediv__
    __rdiv__ = __rtruediv__
