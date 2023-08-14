"""import math
print(math.floor(3.56))
print(math.ceil(3.56))
print(math.floor(8.99))
print(math.ceil(8.99))
sum=100
print("The calculation is of rupees "+str(sum))
print(math.cos(3.6))
a=1
b=3
print(type(a))
str="this is my new coding era!"
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.find("new"))

item1=[1,2,3]
item1[2]="5"
print(item1)

tup1=(4,5,6)
print(tup1)
#tup1=(4,5,6)
#tup1[2]="9"
#print(tup1)
tup1=tuple((4,5,6))
print(tup1)
tup1=(4,5,6)
print(type(tup1))"""

"""dict1={}
print(dict1)
dict1={}
print(type(dict1))
dict1 ["Kunal"] = 100
print(dict1)
dict1 ["Kunal"] = 100
print(dict1.items())
dict1 ["Kunal"] = 100
print(dict1.keys())
dict1 ["Kunal"] = 100
print(dict1.get("Kunal"))
dict1["Shrikant"]=50
print(dict1)"""

"""i=0
while (i<20):
    print(i)
    i=i+1"""

"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)"""

"""veggies=["Tomato","cabbage","cauliflower"]
colours=["red","blue","green"]
for y in veggies:
    for x in colours:
        if(y!="cabbage"):
            print(y,x)"""

"""j = 1
        
while j <= 10:
    if j % 2 == 0:
         print(j)
    j=j+1
        
i = 1

while i <= 10:
    if i % 2 == 0:
        print(i)
    i = i + 1"""

"""for x in range(0,5):
    for y in range(0,x+1):
        print("*",end="")
    print() """

'''for x in range(0,5):
    for z in range(0,5-x):
        print(" ",end="")
    for y in range(0,x+1):
        print("*",end="")
    print() '''
    
"""i=5
while i:
    for x in range(0,5):
        print("*",end="")
    i=i-1
    print()"""

"""i=5
while i:
    for z in range(0,5-i):
        print(" ",end="")
    for x in range(0,i):
        print("*",end="")
    i=i-1
    print()"""


"""for i in range(5,0,-1):
    for z in range(0,5-i):
        print(" ",end="")
    for x in range(0,i):
        print("*",end="")
    print()"""

alphabet=["a","b","c","d","e"]
for i in range(0,5):
    for y in range(0,i+1):
        print(alphabet[y],end="")
    print()

    