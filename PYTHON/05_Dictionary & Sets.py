# Dictionary is a collection of "Key-Value" pair
mydict={
    "Python":"A dynamically typed language", #Each line in a dictionary must be seperated by using comma
    "Html": "A language which is used for website creation",
    "anotherdict":{'Html':'Web developement'}, #Nested dictionary
    "seconddict":{'Java':'A programming language'}
}
mydict["Python"]=["An user efficient language"] #we can change the value of the key
print(mydict["Python"])
print(mydict["anotherdict"]['Html'])
print(mydict["seconddict"]["Java"])
#Properties of dictionary
# 1. It is unordered(arrangement of this item is not in a specific order)
# 2. It is mutable(changeable)
# 3. It is indexed
# 4. It cannot contain duplicate key
