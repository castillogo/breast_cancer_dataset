#
# data types in Python
#
# ... which data types do you know?

# integer, float, string, list, dictionary, tuple, boolean, object, set, NoneType

n = None
a = 1
b = 1.5
c = 'hello'
d = "Tom O'Malley"
e = 'Obi Wan said: "these are not the droids you are looking for"'
f = [1, 2, 3]
g = {'color': 'blue', 'height': 123.4}
h = {'colors': ['blue', 'green', 'red'], 'height': 123.4}
i = [c, f, g]
j = (c, f, g)
k = True
m = {'blue', 'green', 'blue', 'red'}

# check types
type(g)
type(f[1])

#
# taxonomy of data types
#
datatypes = {int, float, str, list, dict, tuple, bool, set}

primitive = {bool, int, float, str, None}
composite = {list, dictionary, tuple, set}

mutable = {list, dict, set}
datatypes.difference(mutable)
immutable = datatypes.difference(mutable)

#
# Type Conversions
#
datatypes = {int, float, str, list, dict, tuple, bool, set}
a = 7
float(a)
str(a)
bool(a)
a = 0
bool(a)

s = "hello"
list(s)
set(s)

set("the quick brown fox jumps over the lazy dog")

s = "777"
int(s)
float(s)
tuple(s)

s = "hello"
list(s)
t = range(5)
t = list(t)

dict(zip(s, t))
list(zip(s, t))

k = [['hund', 'dog'], ['katze', 'cat'], ['fisch', 'fish']]
dict(k)

x = list(s)
str(x)
''.join(x)

#
# boolean conversions: guess the result
#
bool(0)
bool("hello")
bool(None)
bool("0")
bool("")
bool("False")
bool([0])
bool([1])
bool([])
bool({})
bool({0: ""})
bool((0))
bool((0,))

#
# convert column types in pandas
#
import pandas as pd

data = [[1,2,3], list('abc')]
df = pd.DataFrame(data)

df = df.transpose()
df.info()  # all types are still strings

df[0].astype(int)
df[0].astype(float)
