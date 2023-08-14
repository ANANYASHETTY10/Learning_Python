#To store a string using a variable "sentence"
sentence=("I love to sing and dance")
print(sentence)


#To store a string using a function called as ".lower()"
sentence=("I love to sing and dance")
print(sentence.lower())


#To check a string whether it is lower or not by using a function called as ".islower()"
sentence=("I lOve to siNg and dAnce")
print(sentence.islower())


#To check a string whether it is lower or not by using ".lower().islower()" function
sentence=("I love to sing and dance")
print(sentence.lower().islower())


#To store a string using a function called as ".upper()"
sentence=("I love to sing and dance")
print(sentence.upper())


#To check the length of the sentnece using the function "len()"
sentence=("I love to sing and dance")
print(len(sentence))

#To replace a word with another using a function called as ".replace("",""))"
sentence=("I love to sing and dance")
print(sentence.replace("sing","act"))


#To check the index or the position of that specific character we have to start from '0' and spaces between the words are also 
#Using the function ".index("x")" where x being any variable.
sentence=("I love to sing and dance")
print(sentence.index("a"))


#To break a sentence within 2 parts we use a function called as "\n"
print("I love to \n sing and dance")

