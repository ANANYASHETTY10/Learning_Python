# List are containers to store a set of values of any data type
# List are ordered in nature
a=[1,3,56,45,99]
print(a)
# to access any one character from the list
print(a[0])
print(a[3])
# To change the character from a list 
a[0]=14
print(a)
a[4]=18
print(a)
# As list stores different datatype we can create list using those data types
name=["Ananya",11.2,14,False]
print(name)

# List slicing(Same as "string slicing")
name1=["Ananya","Kunal","Shri","Arjun",45]
print(name1[0:3])
# Negative slicing
print(name1[-4:])

# List methods
# 1) List.sort()
L1=[1,55,14,72,9]
L1.sort() #Updates the list in ascending order
print(L1)
L1.reverse() #reverses the actual list "L1"
print(L1)
L1.append(8) #add "8" at the end of the list
print(L1)
L1.insert(2,22) #insert "22" at the index value of "2"
print(L1)
L1.pop(2) #remove the value from index "2"
print(L1)
L1.remove(72) #removes directly specific number mentioned
print(L1)

# Tuple is an immutable (cannot change) data type in python
# How to write a tuple is shown below
t1=(1,4,55,7,18)
# Ways of tuples
t1=() #---> Empty tuple
print(t1)
# t1=(1) ---> Wrong way to declare a tuple with single value
t1=(1,) #--->Right way to decalre a tuple with single value by using a comma
print(t1)

# Tuple methods
t2=(1,34,55,66,74,34)
print(t2.count(34)) #Count the total occurence of "34" in the tuple
print(t2.index(34)) #Return the index value of first occurence of "34" 
