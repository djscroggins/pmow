import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
print(m.maps)
a['c'] = 'E'
print('After : {}'.format(m['c']))
print(m.maps)


print('\nReorder then mutate')
m.maps = (list(reversed(m.maps)))
print('Before: {}'.format(m['c']))
print(m.maps)
b['c'] = 'E'
print('After : {}'.format(m['c']))
print(m.maps)
