import numpy as np

cat1 = [180,30]
#cat1 = np.array([[180, 30], [45, 10], [300, -45]])
cat2 = np.array([[180, 32], [55, 10], [302, -44], [120, -8], [83, 55], [12, 26]])

#cat1 = np.radians(cat1)
#cat2 = np.radians(cat2)
#max_radius = np.radians(5)
max_radius = 5

order = np.argsort(cat2[:,1])
cat2_ordered = cat2[order]
print('cat2_ordered')
print(cat2_ordered)

min_dec = cat1[1] - max_radius
max_dec = cat1[1] + max_radius
print('min and max')
print(min_dec, max_dec)

#index in cat2_ordered
begin = np.searchsorted(cat2_ordered[:,1], min_dec, side='left')
end = np.searchsorted(cat2_ordered[:,1], max_dec, side='right')

print('id of cat2_ordered')
print(begin, end)
print('elements from cat2_ordered')
print(cat2_ordered[begin], cat2_ordered[end])

original_begid, original_endid = order[begin], order[end]
print('id original, cat2')
print(original_begid, original_endid)

print('from original array: cat2')
print(cat2[original_begid], cat2[original_endid])
