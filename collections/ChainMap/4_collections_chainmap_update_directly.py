import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before:', m)
m['c'] = 'E'
print('After :', m)
print('a:', a)

print('\nReorder then mutate')
m.maps = (list(reversed(m.maps)))
print('Before:', m)
m['c'] = 'E'
print('After :', m)
print('b:', b)

