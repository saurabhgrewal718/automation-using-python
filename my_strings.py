var = "yes thjis is a string"
var2 = 'this is a greedy\'s gouse'

# use of three quotes to represent the mulitline input
var = """
whatever i write here 
will appeear as it is 
and it is 
co 
soo 
cool"""
print(var)

#using raw string 
var = r"this is a \' raw string"
print(var)

var = "String slicing"
for i in  range(0,len(var)):
    print(var[i],end=" ")

print("-1 ",var[-1])
print("4 ",var[4])
print("-1 -1 ",var[:-1])
print("all ",var[:])


a ='cats' not in 'cats and dogs' 
print(a)

#strign methods
var = var.upper()
print(var)

var = var.lower()
print(var)

var = var.isupper()
print(var)

a = '12345'.islower()
print(a)