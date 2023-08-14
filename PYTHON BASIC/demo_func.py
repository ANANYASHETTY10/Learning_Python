def get_val():#this function is use to get value of the veriable which is declare
    value  = int(input("enter your value: "))
    return value #return the value which is given by the user

def get_sum(first_no, second_no):#takes the two no. as the input and returns the sum of it
    return first_no+second_no

a = get_val()#call the function to get the value of a from user
b = get_val()#call the function to get the value of b from user
sum = get_sum(a, b)
print(sum)