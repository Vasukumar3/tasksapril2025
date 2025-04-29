#Syntax
# def funcname():
#     #block of code
#     #block of code

# def greet(): #function definition
#     print("this is sample function") #function body
# greet()#function calling




# def add(): #function definition
#     num_1 = input("enter the number 1: ")
#     num_2 = input("enter the number 2:")
#     result = int(num_1) + int(num_2) # ""
#     print(result) # ""
# add()


# def details():
#     user = "durga"
#     id = 1234
#     print(user)
#     print(id)
# details()


# def add(num1,num2):#function defintion
#     print(num1+num2) #function body
# add(15,25)#arguments are passed during function calling
# add(10,10)
# add(100,25)


# def details(name,id):
#     print(f"user {name} and employed id {id}")
# details("rahul",1234)
# details("vasu",123)

# def mul(num1,num2):
#     print(num1*num2)
#     print(num1**num2)
#     print(num1+num2)
#     print(num1/num2)
# mul(5,2)




# def mul(num1,num2):
#     return num1*num2
# obj = mul(5,2)
# print(obj+25)
# obj1 = mul(10,25)
# print(obj1+35)

# def add(a,b):
#     return a+b
# obj = add(10,10)
# print(obj)


# def details(user=None,id=None,dept=None):
#     print(user,id,dept)
# details("vasu",1234,"frontend")
# details("rahul",123)
# details("sai")
# details()


# def mul(a,b=2):
#     return a*b
# # obj = mul(10,5)
# # print(obj)
# print(mul(2,5))
# print(mul(10,15))
# print(mul(15))
# print(mul(15))

#arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)
# def myfunc(*a):
#     print(a)
# myfunc("vasu","kumar",5.7,[1,2,3])

# * --> tuple

#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
#**
# def myfunc(**a):
#     print(a)
# myfunc(a=10,b=20,c=30)
#**--> dict


# *--> tuple *--> all
# **--> dictionary 


# variables --> two types --> local variables --> global variables
#1. local variable ---> function ( inside the function)

# def sample():
#     user = "raju"
#     id = 123
#     print(user,id)
# sample()





# balance = 1000
# def credit(amount):
#     print(amount)
#     print(balance)
#     acc_num = 123456789
#     print(acc_num)
# credit(500)
# print(balance+1000)



# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)
# def div(a,b):
#     print(a/b)




# def credit():

# def withdraw():

# def balance():

# def ministatement():

# def exit():



# balance =1000
# def credit(amount):
#     global balance
#     balance += amount
#     print(balance)
# credit(500)

# def withdraw():
#     pass

"""
Modifying a Global Variable Inside a Function
To modify a global variable within a function, use the global keyword.
Example:
count = 10  # Global variable
def update_count():
    global count  # Access and modify the global variable
    count += 5
    print("Count inside function:", count)
update_count()
print("Count outside function:", count)
# Output:
# Count inside function: 15
# Count outside function: 15
Key Points:
    Local variables are limited to the function scope.
    Global variables are accessible throughout the program but can only be modified inside a function if declared as global.

"""








# atleast 10 python modules --> atleast 2 functions
# import csv


# age = 35
# def voter():
#     global age
#     age_2 = 17
#     age += age_2
#     print(age)
# voter()


