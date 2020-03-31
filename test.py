a = {1: {'a': 'aaa'}, 2: {'b': 'bbb'},}
b = {3: {'c': 'ccc'}, 4: {'d': 'ddd'}, 5: {'e': 'eee'}, 6: {'a': 'aaa'}, 7: {'b': 'bbb'}}

print("a =", a)
print("b =", b)
a_values = a.values()
print("type a_values =", type(a_values))
#print("dir a_values =", dir(a_values))
b_values = b.values()
print("type b_values =", type(b_values))
#print("dir b_values =", dir(b_values))
for i in b_values:
    if not i in a_values:
        print('i =', i)
        #print('index =', b_values.index(i))