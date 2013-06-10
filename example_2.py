# In the following example, we start off with a list of values, and we add some
# new values to them. We now want to find the difference between the mean of
# the original list of values, and the new list of values. This should give
# 0.625 but it gives 0.0 instead. Why is this?

import numpy as np

# Define the original set of values.
values = [8., 7., 9., 4., 6., 7., 8., 4.]

# Create a new list with the original values and add a few more
new_values = values
new_values.append(8.)
new_values.append(9.)
new_values.append(2.)
new_values.append(1.)
new_values.append(5.)

print "Difference in the mean:", np.mean(new_values) - np.mean(values)
