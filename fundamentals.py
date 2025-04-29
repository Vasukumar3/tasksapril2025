#print --> used to display info on the screen
#syntax
# print(exp)
# print(10+10)
# print("*")
# print("**")
# print("***")
# print("****")

# Python standard library

# The Python Standard Library contains the exact syntax, semantics, and tokens of Python. It contains built-in modules that provide access to basic system functionality like I/O and some other core modules. Most of the Python Libraries are written in the C programming language. The Python standard library consists of more than 200 core modules. All these work together to make Python a high-level programming language. Python Standard Library plays a very important role. Without it, the programmers can’t have access to the functionalities of Python. But other than this, there are several other libraries in Python that make a programmer’s life easier. 


# builtins.py is a Python module that contains the built-in functions, exceptions, and objects that are always available in Python. These built-ins are accessible without explicitly importing them because they are part of the Python interpreter's core functionality.
# Purpose of builtins Module

#     Centralized Access: It defines and organizes functions, constants, exceptions, and classes that are essential for Python programs.
#     Always Available: The objects in builtins are automatically imported into every Python script, so you can use them directly.


# The builtins module is part of the Python Standard Library. It is implemented in C in CPython, so you won’t find a builtins.py file but can access its functionality through the Python interpreter.


# below code is used to perform addition operation
# num_1 = 10 #here taken one varible and assign a value 10 by using = operator
# num_2 = 10
# result = num_1+num_2
# print(result)

'''
i have taken two variables
and i assigned values to those variables
and i perform addition operations by using + operator
later, i display the result by using print function
'''

"""


"""

#syntax for variable creation
#var = value

# age = 35
# print(age)
# print(id(age)) 


# height = 5.7
# print(height)

# _second_person_height = 5.5
# print(_second_person_height)

# _1st_person_id = 12345
# print(_1st_person_id)


# name = "vasu"
# namE = "koushik"
# NAME = "hemasai"
# print(id(name))
# print(id(namE))
# print(id(NAME))

# id --> used to identify the memore addresss(object)

# if = 35
# print(if)


#camelCase
# studentName = "lakshmana sai"

# #snake_case
# student_name = "yaswanth"

# #PascalCase
# StudentName  = "naveen"


# number = 123
# print(type(number))

# height = 5.71254
# print(type(height))


# student_name = "saranya@123"
# print(type(student_name))


# from builtins import print


# sentence = 'welcome to pythonlife 7'
# sentence_2 = "attend python session 7 O'clock"
# sentence_3 = ''' he said , " welcome to pythonlife 
# attend python sessions 7 O'clock"
# '''
# print(type(sentence))
# print(type(sentence_2))
# print(type(sentence_3))

# string used to store textual information and also represent seq of characters





#type conversion
# age = 35
# print(type(age))

#int ---> float
# age = 35
# print(age)
# float_conversion = float(age)
# print(type(float_conversion))


#float ---> int
# height = 5.7
# int_conversion = int(height)
# print(int_conversion)


# int --> string
# student_id = 12345
# str_con = str(student_id)
# print(type(str_con))


#str ---> int
# student_id = "12345"
# int_conv = int(student_id)
# print(type(int_conv))

#float --> str
# height = 5.7
# str_conv = str(height)
# print(type(str_conv))



#type conversion --> implicit type conversion(automatic) 2. explicit type conversion(manual)



# num_1 = 10
# num_2 = 5.7
# print(num_1+num_2)

# num_1 = float(input("enter number "))
# num_2 = float(input("enter number 2: "))
# result = num_1+num_2
# print(result)


# name = "10"
# surname = "10"
# print(name+surname)




# height = "5.7"
# print(type(height))



######### april 07 2025 ###############
# **Lists:**

# - A list is a mutable, ordered sequence of elements.
# - Elements can be of different data types.
# - Lists are defined using square brackets `[]`.

# list_1 = [1,5.7,"srinivas",[2,35.5,"shiva"],(1,5.7,"koushik"),1,1,1,2,2,2,]
# print(list_1)
# list_1.append("srikranth")
# print(list_1)



# # tuples
# tuple_1 = (1,5.7,"koushik",[1,2,3],(1,2,3),1,5.7,"35")
# print(type(tuple_1))





# set_1 = {"yaswanth","kiran","gridhar",105,25,35,"yaswanth","kiran","11",11,5.7,5.7,(1,2,3),}
# print(type(set_1))
# print(set_1)





# dict_1 = {
#     "user1":"user1@123",
#     "user2":"user2@123",
#     "user3":"user#@123",
# }
# print(dict_1)




# emp_id = {
#     1:"rohit",
#     2:"ramya",
#     3:"ram",
#     4:"pythonlife",
#     (1,2):5.7,
#     "user1":["vasu",1234,"frontend"],
#     5:5.7,
# }
# print(emp_id)





# list_1 = [1,2,3,4,1,1,2,3,4,"vasu","kumar","lokesh","ramya","ramya","lokesh"]
# print(type(list_1))
# set_con = set(list_1)
# print(set_con)
# list_con = list(set_con)
# print(list_con)



#list --> tuple
#tuple --> list
#list --> set
#set ---> list
#dict --> tuple --> observation
#tuple --> dict --> observation




#boolean
# sample = True
# print(type(sample))


# print(bool(1))
# print(bool(0))


#complex data type


# In Python, a complex data type is used to represent complex numbers. A complex number consists of a real part and an imaginary part, and it’s written in the form a + bj


# a → Real part (float or int)
# b → Imaginary part (float or int)

#mathematical operations
# a = 5+5j
# b = 10+5j
# result = a+b
# # print(type(a))
# print(result)


# Take the user's age as input and print a message using that input.
age = int(input("enter user age: "))
print("user age", age+5)



