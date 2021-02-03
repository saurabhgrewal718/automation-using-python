# # # spam = ['cat', 'bat', 'rat', 'elephant'] 
# # # for i in spam:
# # #     print(i)

# # # for i in spam:
# # #     if 'b' in i:
# # #         continue
# # #     print(i)

# # # # empty list
# # # my_list = []

# # # # list of integers
# # # my_list = [1, 2, 3]

# # # # list with mixed data types
# # # my_list = [1, "Hello", 3.4]

# # # # nested list
# # # my_list = ["mouse", [8, 4, 6], ['a']]
# # # print(my_list[0])
# # # print(my_list[1])
# # # print(my_list[0][3])
# # # print(my_list[1][2])

# # # # Negative indexing in lists
# # # my_list = ['p','r','o','b','e']

# # # print(my_list[-1])

# # # print(my_list[-5])


# # my_list = ['p','r','o','g','r','a','m','i','z']

# # # elements 3rd to 5th...last ellemnt not included...form index 2 to 4
# # print(my_list[2:5])

# # # elements beginning to 5th...5 elements in total...index 5 not included
# # print(my_list[:5])

# # # elements 6th to end
# # print(my_list[5:])

# # # elements beginning to end
# # print(my_list[:])


# # # Correcting mistake values in a list
# # odd = [2, 4, 6, 8]

# # # change the 1st item    
# # odd[0] = 1            

# # print(odd)

# # # change 2nd to 4th items
# # odd[1:4] = [3, 5, 7]  

# # print(odd) 

# # # Deleting list items
# # my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# # # delete one item
# # del my_list[2]

# # print(my_list)

# # # delete multiple items
# # del my_list[1:5]

# # print(my_list)

# # # delete entire list
# # del my_list

# # # Error: List not defined
# # print(my_list)


# # my_list = ['p','r','o','b','l','e','m']
# # my_list.remove('p')

# # # Output: ['r', 'o', 'b', 'l', 'e', 'm']
# # print(my_list)

# # # Output: 'o'
# # print(my_list.pop(1))

# # # Output: ['r', 'b', 'l', 'e', 'm']
# # print(my_list)

# # # Output: 'm'
# # print(my_list.pop())

# # # Output: ['r', 'b', 'l', 'e']
# # print(my_list)

# # my_list.clear()

# # # Output: []
# # print(my_list)

# my_list = [3, 8, 1, 6, 0, 8, 4]
# l2 = my_list.copy()
# print("copy ofmy_list ",l2)

# l2 = my_list.copy()
# l2.reverse()
# print("reversed list",l2)

# l2 = my_list.copy()
# l2.sort()
# print("sorted list ", l2)

# coutning = my_list.count(0)
# print("how many perticular valeus are perent in a list " ,coutning)

# # vowels list
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# # count element 'i'
# count = vowels.count('i')

# # print count
# print('The count of i is:', count)

# # count element 'p'
# count = vowels.count('p')

# # print count
# print('The count of p is:', count)

# print(my_list.index(3))

# #clear() - Removes all items from the list
# l2 = my_list.copy()
# print(l2)
# l2.clear()
# print(l2)

# l2 = my_list.copy()
# #pop() - Removes and returns an element at the given index
# print(l2.pop(2))
# print(l2)

# #extend() - Add all elements of a list to the another list
# # languages list
# languages = ['French', 'English']

# # another list of language
# languages1 = ['Spanish', 'Portuguese']

# # appending language1 elements to language
# languages.extend(languages1)

# print('Languages List:', languages)

# #If you need to add an element to the end of a list, you can use the append() method.

# a1 = [1, 2]
# a2 = [1, 2]
# b = (3, 4)

# # a1 = [1, 2, 3, 4]
# a1.extend(b) 
# print(a1)

# # a2 = [1, 2, (3, 4)]
# a2.append(b)
# print(a2)


# #The in and not in Operators
# #single assingment statement to check weather a numbe ris in the list or not! 
# print(3 in my_list)
# print(100 not in my_list)

# #Python enumerate()
# # The enumerate() method adds counter to an iterable and returns it (the enumerate object).

# # The syntax of enumerate() is:

# # enumerate(iterable, start=0)

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))


grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)