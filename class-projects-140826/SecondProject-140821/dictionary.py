__author__ = 'Ben Setzer'

d1 = {'able': 23, 'baker': 44, 'charlie': -23}

print(d1['able'])
#print(d1['easy'])
d1['easy'] = 99
print(d1)

for x in d1:
    print(x, d1[x])
