from functools import partial
from mpmath import power

square = partial(power, exponent=2)
cube = partial(power, exponent=3)


def sqaure( ):
    pass


print(sqaure())