import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child(c)

print(f'm1.map = {m1.maps}')
print(f'm2.map = {m2.maps}')
print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))
