# The following code should compute the integral of the function
#
# y = 3. * x ** 2 + 2. * x + 1.
#
# defined by the x and y arrays, between 0 and 10. This should give 1110.0 but
# instead gives 2100.0:
#
# $ python example_3.py
# Integral is: 2099.999499
#
# why is this not working?

import numpy as np
from scipy.integrate import trapz

n = 1000
x = np.linspace(0., 10., n)
y = 3. * x ** 2 + 2. * x + 1.

print "Integral is:", trapz(x, y)
