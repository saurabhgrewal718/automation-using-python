# #coditional
# name = 'Mary'   
# password = 'swordfish'   
# if name == 'Mary':
#     print('Hello, Mary')        
#     if password == 'swordfish':
#         print('Access granted.')        
#     else:         
#         print('Wrong password.')

# #elif statements
# name = 'Carol' 
# age = 3000 
# if name == 'Alice':     
#     print('Hi, Alice.') 
# elif age < 12:     
#     print('You are not Alice, kiddo.') 
# elif age > 2000:     
#     print('Unlike you, Alice is not an undead, immortal vampire.') 
# elif age > 100:     
#     print('You are not Alice, grannie.')

# #using while loops vs using if statement for the same
# spam = 0 
# if spam < 5:     
#     print('Hello, world.')     
#     spam = spam + 1

# while spam < 5:
#     print('hello world')
#     spam = spam+1

# #annoying program name....input your name and it will keep on asking you to input your name untill you enter the ringht name
# name = 'Saurabh'
# name2 = input('Enter your name : ')
# while name!=name2:
#     print("Jhooth mat bol bhai...sahi nam bata apna")
#     name2=input('Enter your name : ')

#break statements-------------------------------------------------------
#diffrent kind of annoyence-- keep on asking the name untill you write the correct name
# while True:
#     name = input("Naam bata apna : ")
#     if name.lower() == "saurabh":
#         print("hmm sahi jawab! chalo niklo ab! ")
#         break
#     else:
#         print("Jhooth mat bol bhai...sahi nam bata apna")

#When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition
#password game

# while True:
#     name = input("han bhai tera naam ? : ")
#     if name.lower() != 'saurabh':
#         continue
#     print("han bhai "+ name + " ! Welcome...! ")
#     while True:
#         passw = input("Password bata... : ")
#         if passw != 'swordfish': 
#             print('Galat password hai bhai...tu '+ name + " hi hai naaaa? ")
#         else:
#             print("Access granted")
#             break
#     break


#password game-- password bata leking try password batane ki bas 3 hongi

while True:
    name = input("han bhai tera naam ? : ")
    if name.lower() != 'saurabh':
        continue
    print("han bhai "+ name + " ! Welcome...! ")
    count = 0
    limit = 3
    while count<limit:
        passw = input("Password bata... : ")
        count+=1
        if passw != 'swordfish':
            if(limit-count>0): 
                print('Galat password hai bhai...tu '+ name + " hi hai naaaa? " + str(limit-count)+" try aur rah gai! sahi password bhar..varna lock out hjo jaiega 2 din ke liye! ")
            else:
                print('lag gai bhai teri to.... 2 din ke liye lock hogya ab to tu ! hahahahah')
        else:
            print("Access granted")
            break
    break
