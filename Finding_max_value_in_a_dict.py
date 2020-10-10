d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = (d.keys())
# initialize variable best_key_so_far to be the first key in d
max_value=d['a']
for k in ks:
    if d[k] > max_value:
        max_value= d[k]
print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

ks = d.keys()
best_key_so_far = list(d.keys())[0]  # Have to turn ks into a real list
                                #before using [] to select an item
for k in ks:
# check if the value associated with the current key is
# bigger than the value associated with the best_key_so_far
# if so, save the current key as the best so far

    if d[k] > d[best_key_so_far]:
        best_key_so_far = k

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))
