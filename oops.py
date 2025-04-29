#syntax
# class cn(): #class definition
#     class body

# class details():#class definition
#     name = "ramesh" #attributes
#     name_2 = "ajay" #attributes
#     def details1(self): #methods 1
#         print("this is first method")
#     def details2(self): #methods 2
#         print("this is second method")
# #Syntax
# # obj_name = class_name()
# obj = details() #
# print(obj.name)
# print(obj.name_2)
# obj.details1()
# obj.details2()



# class mobiles():
#     brand_name = "samsung"
#     brand_color = "white"
#     storage = "128GB"
#     def calling(self,brand):
#         print("you are calling... from",brand)
#     def camera(self):
#         print("capturing photo....")
#     def browsing(self,):
#         print("you are browsing")
#         self.camera()
#         self.calling("iphone")


# #objname = classname()
# samsung  = mobiles()
# samsung.calling("samsung")
# # samsung.camera()
# # samsung.browsing()
# # print(samsung.storage)
# vivo = mobiles()
# vivo.calling("vivo")

# iphone = mobiles()
# iphone.browsing()


# class car():
#     def __init__(self,bn,color,model,):
#         self.bn = bn
#         self.color = color
#         self.model =model
#     def driving(self):
#         print("you are driving",self.bn)
#     def engine(self,engine):
#         print("start/off",self.model)
#         print(f"engine version {engine}")
# tata = car("tata","white","2023")
# tata.driving()
# maruti = car("maruti","black","2024")
# maruti.driving()
# inova = car("inova","brown",2020)
# inova.engine("v6")


# class mobilephone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number}  from {self.brand} {self.model}")
#     def send_message(self,number,message):
#         print(f"sending {message} to {number} {self.brand} {self.model} ")
# class smartphone(mobilephone):
#     def app(self,appname):
#         print(f"using {appname} app on {self.brand}  {self.model}")

# sphone = smartphone("apple","iphone16")
# sphone.make_call(1234567890)
# sphone.send_message(1234567890,"hello")
# sphone.app("spotify")



# class GrandFather:
#     def output(self):
#         print('this is gf class')
# class Father(GrandFather):
#     def outputf(self):
#         print('this is father class')
# class Child(Father):
#     def outputChild(self):
#         print('this is child class')  
# obj = Child()
# obj.output()
# obj.outputf()
# obj.outputChild()




# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")
# obj = b()
# obj.parent()
# obj.child1()

# obj2 = c()
# obj2.parent()
# obj2.child2()




# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")

# obj = child()
# obj.father()
# obj.mother()
# obj.child()






# class ATM():
#     def __init__(self,bank_name,branch_name,color):
#     def account():

    
#     def credit():

#     def withdraw():

#     def ministatement():
# class ATM2():
#     def balance enquiry()

#     def login()










###############   april 23 2024 ########
#polymorphism: implementing same thing in different forms
#overloading ---> 1. operator overloading 2. method overloading
#method overiding

# "+" --> operator overloading
# a = 10
# b = 20
# print(a+b)


# a = "10"
# b = "20"
# print(a+b)

# a = 10
# b = 20
# print("a"*20)


# 2.method overloading --->
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments


#sample
# class sample():#class definition
#     def add(self,a,b):
#         print(a,b)
#     def sub(self,a,b):
#         print(a,b)
#         self.add()
# objname = classname()
# obj = sample()
# obj.sub("lokesh",1234)



# 2.method overloading --->
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments


# class sample():#class definition
    # def add(self,a,b):
    #     print(a,b)
#     def add(self,a,b,c=None,d=None):
#         print(a,b,c,d)
# obj = sample()
# obj.add(10,20)
# obj.add("vasu","lokesh")
# obj.add(10,20,1234)



# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):  # Method overloading with different parameters
#         return a + b + c

# # Create an instance of the Calculator class
# calc = Calculator()

# # Call the overloaded methods
# print(calc.add(2, 3))     
# print(calc.add(2, 3, 4))  





# 2.method overloading --->
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments


# class sample():#class definition
#     def add(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj = sample()
# obj.add(1,2,3)
# obj.add(1,2)
# obj.add(1)
# obj.add()
# obj.add("hello","python","students")
# obj.add("hello","python")
# obj.add("hello")
# obj.add()



# 2.method overriding--> method name should be same, arguments should be also same
# class father():
#     def details(self,a):
#         print("this is father class")
#         print(a)

#     def add(self,a)
# class child(father):
#     def details(self,a):
#         print("this is child class")
#         print(a)
#         super().details(1234)
# obj = child()
# obj.details("100cr")




# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _


# class Gfather():
#     def __init__(self,a):
#         self.__a = a
#         print(a)
# class father(Gfather):
#     def display(self):
#         print(self.__a)
# obj = father("100cr")
# obj.display()



#ATM



############# april 24 2025 ##################
#abstraction --> hiding the implementation and showing only essential part

# 1.abstract class --> class which contain abstract methods is called abstract class
# 2.abstract method --> the method which is having only declaration but not the definition is called abstract method (hiding the implementation)
# class which does not have abstract method is called concrete class
# concrete class  --> class without abstract methods
# object cannot create for abstract class
# object can create only concrete classes
# To create abstract classes in Python, you can use the abc (Abstract Base Classes) module


# from abc import ABC, abstractmethod
# class abstract_demo(ABC):
#     @abstractmethod
#     def display(self):
#         pass
#     @abstractmethod
#     def display2(self):
#         pass
# class demo(abstract_demo):
#     def display(self):
#         print("implementing in derived class")
#     def display2(self):
#         print("implementing in derived class display2")
# obj = demo()
# obj.display()
# obj.display2()


# from abc import ABC, abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def payment_processing(self):
#         pass

# class gpay(payment):
#     def payment_processing(self,amount):
#         print(f"processing {amount} using gpay")
# class phonepe(payment):
#     def payment_processing(self,amount):
#         print(f"processing {amount} using phone pe")
# obj = gpay()
# obj.payment_processing(1000)
# obj2 = phonepe()
# obj2.payment_processing(500)

# from abc import ABC, abstractmethod   
# class Car(ABC): 
#     @abstractmethod  
#     def mileage(self):   
#         pass  
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
#     def smartfeaturs(self):
#         print("providing additional functionalities")
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ") 













