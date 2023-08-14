# Strings ia a sequence of characters enclosed in a quote and it is one of the datatype
a="32"
print(a)
print(type(a))

# Single quoted string
a='python'
print(a)
# Double quoted string
a="Python's"
print(a)
#  Triple quoted string
a='''Python"s and python's'''
print(a)

# (Addition of two strings)
greetings = "Good afternoon,"
name="Ananya"
c= greetings + name
print(c)

# Index of the variable starts from 0 to L-1 where L is total length of variable
name ="Python"
print(name[2])
print(name[0])
# You can access a character from a string but cannot change the character from the string
# Like--> name[3]="d"-->does not work

# String Slicing
# In this,string is been sliced to get a specific part of string by giving the index range
name="Java"
print(name[0:3]) # Here characters will be printed from "0" to "2" excluding "3"
# We can also write it as 
print(name[0:]) #---> same as [0:4]
# or
print(name[:4]) #---> same as [0:4]

# Negative index is used to access the last character of string i.e "-1"
name="Scalar"
print(name[-4:-1]) #"scalar" have the index of "0 to 5" and Negative index of "-6 to -1"
# We have to write the code in the range of "-6 to -1"

# Slicing with skip value
# Sometimes we need skip some character in the string so we need "slicing with skip value"
name="Amazon"
print(name[1:4:1])#The character will not skip cause the value is "1"
print(name[1:4:2])#The character will be skipped here by "1"
print(name[1:5:1])
print(name[1:5:3])
print(name[0:5:1])
print(name[0::5])
print(name[0:-1])

# String Function
sentence="python is a prograaming language.python is simple and very adaptive to learn"
print(len(sentence))#This function returns the length of the string(including spaces)
print(sentence.endswith("learn"))#This function will tells whether the string is ended with the provided word or not
print(sentence.endswith("easy"))
print(sentence.count("is")) #It will count the total no. of occurence of any character
print(sentence.capitalize()) #It capitalize the starting letter of gthe string
print(sentence.find("is")) #It finds the index value of only first occurence of that word in the string
print(sentence.replace("python","Java"))#It replaces old word with new word in the entire string

sentence_1="Python is a language.\nPython\t is ve\\ry eas\'y to learn."
print(sentence_1)#Escape sequence character comprises of one or more character but while represented in string it is of one character
