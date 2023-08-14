# Write a program to store seven fruit names in a list entered by the user
f1=input("Enter the Fruit number 1= ")
f2=input("Enter the Fruit number 2= ")
f3=input("Enter the Fruit number 3= ")
f4=input("Enter the Fruit number 4= ")
f5=input("Enter the Fruit number 5= ")
f6=input("Enter the Fruit number 6= ")
f7=input("Enter the Fruit number 7= ")
myfruits=[f1,f2,f3,f4,f5,f6,f7]
print(myfruits)

# Write a python program to enter the marks of 6 students and display them in a sorted manner
m1=int(input("Enter the mark of STUDENT 1= "))
m2=int(input("Enter the mark of STUDENT 2= "))
m3=int(input("Enter the mark of STUDENT 3= "))
m4=int(input("Enter the mark of STUDENT 4= "))
m5=int(input("Enter the mark of STUDENT 5= "))
m6=int(input("Enter the mark of STUDENT 6= "))
marks=[m1,m2,m3,m4,m5,m6]
marks.sort()
print(marks)

# Check that a tuple cannot be changed in python
t1=(1,3,4,5,6)
t1[0]=9
print (t1)

# Write a program to sum a list with 4 numbers
L1=[1,3,5,77,99]
print(L1[0] + L1[1] +L1[2] +L1[3] +L1[4])
# or
print(sum(L1))

# Write a python program to count the number of zeroes in following tuple
Tuple1=(7,0,8,0,0,9,1,2,0)
print(Tuple1.count(0))