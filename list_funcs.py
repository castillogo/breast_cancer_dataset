"""
common list methods
"""
a = list(range(10))

# indexing
a[5]

# slicing
a[:3]
a[3:6]
c[::-1]
c[::-2]

# concatenate
b = [11, 1, 7]
c = a + b

# methods
a.append(10)
c.sort()
c.reverse()
c.remove(10)
c.pop()

import random
random.shuffle(c)

# check
7 in c
