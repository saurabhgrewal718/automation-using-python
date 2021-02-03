# # #def functionname( parameters ):
# # #    "function_docstring"
# # #    function_suite
# # #    return [expression]

# # def sayHello(name):
# #      print('Hello, ' + name)

# # sayHello('Al')

# # #the call stack in a function
# # def a():
# #     print("a started")
# #     b()
# #     d()
# #     print("a returned")

# # def b():
# #     print("b starts")
# #     c()
# #     print('b returns')

# # def c():
# #     print("c started")
# #     print("c returned")

# # def d():
# #     print("d stared")
# #     print("d returned")
# # #calling the main a function
# # a()


# # def spam(divideBy):
# #     try:
# #         return 42 / divideBy
# #     except ZeroDivisionError:
# #         print('Error: Invalid argument.')

# # print(spam(2))
# # print(spam(12))
# # print(spam(0))
# # print(spam(1))


# # #This program will create a back-and-forth, zigzag pattern
# import sys,time
# indent = 0
# incindent = True

# try:
#     while True:
#         print(" "*indent,end="")
#         print("*********")
#         time.sleep(0.1)

#         if incindent:
#             indent = indent+1
#             if indent == 20:
#                 incindent = False
#         else:
#             indent = indent - 2
#             if indent == 0:
#                 incindent = True
        
# except KeyboardInterrupt:
#     sys.exit()


def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code
evenOdd(2)
evenOdd(3)

#Built-in Functions
#The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.


#all == checks weather all elements in the list are true or not---any value other than 0 and none are true! 
#can be used to check weather an iterable has 0 or none vlaues in them! 
mylist = [1, 1,23,4,42,4,25,25,562,7,246,0]
x = all(mylist)
print(x)

#any()
#Check if any of the items in a list are True: cn be used to find weather in a lidt of 0 or none is there any element which is true

mylist = [False, True, False]
x = any(mylist)