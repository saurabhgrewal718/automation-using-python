# print('My name is') 
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')

# #specifying the range from this to this...last is not included
# print("-------------------")
# for i in range(0,10):
#     print(i)

# #step up by 2
# print("-------------------")
# for i in range(0,11,2):
#     print(i)

# #teacher was angry on you...and gave you to add all numbers from 0 to 100
# print("-------------------")
# num = 0
# for i in range(0,101):
#     num = num + i
# print(num)

# #finding out element sin a list
# print("-------------------")
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))


# #this is the main syntax of the for loop
# #for <var> in <iterable>:
# #    <statement(s)>

# #now lets discuss the iterables in much more details so that it can be easy for us to make sure that we are doing it the right way! 
n1='foobar'                             # String
for i in n1:
    print(i,end=",")

print('\n')
n2=['foo', 'bar', 'baz']                # List
for i in n2:
    print(i,end=" and ")

print('\n')
n3 = ('foo', 'bar', 'baz')                # Tuple
for i in n3:
    print(i,end=" or ")
print('---------------')
for i in range(len(n3)):
    print(n3[i])

print('\t')
n4 = {'foo', 'bar', 'baz'}                # Set
for i in n4:
    print(i,end=" # ")
    
n5 = {'foo': 'namu', 'bar': 'guddu', 'baz': 'they do bhai'}      # Dict
print('-------dict------keys--------')
for i in n5:
    print(i)

print('-------dict 2-----index of the keys--------')
for i in n5:
    print(n5[i])

print('-------dict 3-------values of the keys--------')
for i in n5.values():
    print(i)


#int,float,built-in functions cannot be iterated
print('giving more than one valeus at once of the tuple')
i,j = (90,100)
print(i,j)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i*i, j*j)

d = {'foo': 1, 'bar': 2, 'baz': 3}
items = list(d.items())
print(items)
for i,j in items:
    print("key:"+str(i),"value:"+str(j),sep=",")