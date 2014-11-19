__author__ = 'Ben Setzer'


list1 = ['abel', 'baker', 'charlie', 'dog','int']
x = 73
list2 = ['apple', 73, 'banana', ['a', 34], list1, x, x*x-3,]
print(list1)
print(list2)
print( "=====================")
print(list1[0])
list2[3] = 44
print(list2)
#list1[100] = 33
print(list1)
print( "=====================")

list1 = ['abel', 'baker', 'charlie', 'dog','int']
print(list1)
list1.append('easy')
print(list1)
list1.insert(2, 'fox')
print(list1)
list1.insert(-1,'george')
print(list1)
print(list1[-2])
print("=====================")
print(list1[0:3])
print(list1[1:3])
print(list1[2:-1])
print(list1[2:])
print("===================")

for x in range(0,13):
    print(x)

for x in list1:
    print(x)

print([x[0] for x in list1])

print("===================")

tuple1 = ('able', 'baker', 'charlie', 'dog')
print(tuple1)
print(tuple1[-1])
#tuple1[0] = 'artichoke'


print("===================")

for x in tuple1:
    print(x)


print("===================")

tuple1 = ('hello',)

for x in tuple1:
    print(x)


print("===================")
print('length of list1', len(list1))