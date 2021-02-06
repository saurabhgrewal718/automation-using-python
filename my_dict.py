# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# for i in myCat:
#     print(i)

# for i in myCat.values():
#     print(i)

# for i in myCat.keys():
#     print(i)

# for i,j in myCat.items():
#     print(i,j)

# #in dict order did not matter 
# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# myDog = {'color': 'gray','size': 'fat', 'disposition': 'loud'}

# print(myCat==myDog)

#birthday program
# birthdays= {"manu":"19 august","guddu":"7 july","mummy":"25 march","papa":"5 nov"}
# while True:
#     nme = input("find people : ")
#     if nme=="":
#         break
#     if nme in birthdays:
#         print(birthdays[nme])
#     else:
#         new_name = nme
#         date= input("Enter the DOB : ")
#         birthdays[new_name]=date
#         print("Database sucessfully Updated...!")

# for i in birthdays.keys():
#     print(i)


# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# #since egggs is not present in the list we accessed it by using the get...and giving it a default value of 0
# print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')


#The setdefault() Method
# we usually do this------------
# spam = {'name': 'Pooka', 'age': 5} 
# if 'color' not in spam:
#     spam['color'] = 'black'
 
# we can d this also by doung this--

# spam = {'name': 'Pooka', 'age': 5} 
# spam.setdefault('color', 'black')
# spam.setdefault('color','white')

# for i in spam.items():
#     print(i)


# message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
# count = {} 
 
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1 

# print(count)


import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} 
 
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1 
 
pprint.pprint(count)


