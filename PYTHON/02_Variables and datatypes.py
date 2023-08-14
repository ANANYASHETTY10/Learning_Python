# Variable is a container which stores some given values
a=100
b='ananya'
c=32.25
d=True
print(a)
print(b)
print(c)
print(d)

# To know what are the types of variable is listed above use "type()"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Mathematical Operators in python are
# Arithmetic(+,-,*,/), Assignment(=,+=,-=), Logical(and,or,not) & Comparison(==,>,<,>=,!=)

# Arithmetic Operator
print(a+c)
print(a-c)
print(a*c)
print(a/c) 
# or 
print('The sum of 100 & 32.25 is',100+32.25)
print('The sum of 100 & 32.25 is',100-32.25)
print('The sum of 100 & 32.25 is',100*32.25)
print('The sum of 100 & 32.25 is',100/32.25)

# #Assignment Operator 
a +=2
print (a)
a -=2
print(a)
a *=3
print(a)
c /=5
print(c)

#  Comparison Operator(Gives boolean values)
d=(444<111)
print(d)
d=(444>111)
print(d)
d=(444<=111)
print(d)
d=(444>=111)
print(d)

# Logical operator
bool1=True
bool2=False
print ('The value of bool1 & bool2 is',bool1 and bool2)
print ('The value of bool1 & bool2 is',bool1 or bool2)
print ('The value of bool1 & bool2 is',not bool2) # 'not' will reverse the value of 'bool2' or any provided value

#Typecasting is used to convert one data type of a variable to another data type
a="30"
a= int(a)
print(type(a))
print(a + 60)
print('The sum of 30 & 60 will be',30+60) #additional part
# "30" it's a string literal and 31 is a numeric literal

#Input function
# This fucntion is used to take the input from the keyboard as the string
a =input('Enter a number= ')
a=int(a)
a +=3
print(type(a))
print(a)    


