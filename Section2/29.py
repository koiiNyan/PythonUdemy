# Question:  Please write a function that calculates liquid volume in a sphere
# using the following formula. The radius r  is always 10, so consider making it
# a default parameter.

import math
def liq_vol(h):
    r = 10
    pi = math.pi
    res = ((4 * pi * (r ** 3)) / 3) - ((pi * (h ** 2) * (3 * r - h)) / 3)
    return res

print(liq_vol(2))
