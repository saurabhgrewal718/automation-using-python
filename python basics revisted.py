# #strig concatination and replication
# #correct forms
# n1='Alice'
# n2='Bob'
# n3=5
# print(n1+n2)
# print(n1*n3)


# #incorrrect forms
# print(n1+n3)
# print(n3+n2)
# print(n1*n2)

# #A variable is like a box in the computer’s memory where you can store a single value
# #You’ll store values in variables with an assignment statement.
# var1=45
# var2=46
# var2=var1

# #print()
# print('values: in the object form, seperator: Optional[Text] = ..., end: Optional[Text] = ..., file: Optional[_Writer] = ..., flush: bool = ...')
#values are not optional we need to pass them but we can pass other things as well
print('these are simpley the values')

#sep
print('val1','val2','val3',sep=' @ ')

#end
print('val1','val2','val3',end=',')

#flush - deltes it from the memory

#file
filename = open('python.txt','w')
print('val1','val2','val3',file=filename)
filename.close()

#combining them all 
print('val1','val2','val3',sep=',',end='#',file=filename)

#using \n-newline,\t-tab,\v-vetical tab,\f-puts it first and \r-removes
s = 'Hi there, \nHow are You?'
s1 = 'Hi there,\tHow are You?'
s2 = 'Hi there,\vHow are You?'
s3 = 'Hi there,\fHow are You?'
s4 = 'Hi there,\rHow are You?'
 
print(s)
print(s1)
print(s2)
print(s3)
print(s4)

#we often use the conversion functons lke str() or int()....it can also be done by only character strings
value = 100000
text = 'Tutorial Gateway'
science = 1.20023456341
cr = 'u'
 
print('%d' %value)
print('%i' %value)
print('%u' %value)
print('%o' %value)
print('%x' %value)
print('%X' %value)
 
print('%f' %science)
print('%e' %science)
print('%E' %science)
 
print('%g' %science)
print('%G' %science)
 
print('%c' %cr)
print('%s is a string representation' %value)
print('%s' %text)

#multiplying the \n three times will give us three new lines
print(3 * "\n")
 
print("--------")
print('\n\n\n\n\n')

#special characters in the python functions to use the "" or ''
s = 'Hi there, "How are You?"'
s1 = 'Hi there, \"How are You?\"'
 
print(s)
print(s1)
 
print('I Can\'t Do that')
print('I Don\'t Know you')

#since the values can be the objects we cna use any type
name = 'Tutorial Gateway'
person = 'suresh'
year = 2019
 
#all these formats are the same
print('%s is working at %s' %(person, name))
print('Copyright %s at %d' %(name, year))
print('{0} is working at {1}'.format(person, name))
print('Copyright {} at {}'.format(name, year))
print(person, ' is working at ', name)
print(person + ' is working at ' + name)


# #input()
# name=input('enter your name')
# #it just takes one argument
# print('your name is '+ name)


