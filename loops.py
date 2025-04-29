#syntax
# for variable in sequence:
#     # code to be executed


# voter_list = ["vasu","poojitha","lakshmana","hemasai","srinivas"]
# for i in voter_list:
#     print(f"{i} eligible to vote")
#     number = int(input("Enter the number: "))
#     if number%2==0:
#         print(f"{number} is even number")
#     else:
#         print(f"{number} not even number ")



# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# for i in range(10):
#     print(i)


# for i in range(99,150):
#     print(i)

# for i in range(1,11,5):
#     print(i)


# #multiplication of tables
# for i in range(1,21):
#     print(f"2 X {i} = {i*2}")


# for i in range(1,11):
#     print(f"17 X {i} = {i*17}")


# num = int(input('enter the multiplication table: '))
# for i in range(1,21):
#     print(f"{num} X {i} = {num*i}")



#nested for loop syntax
# for var in iter: #outer for loop
#     for var in iter: #inner for loop  



# for i in range(5):#outer for loop
#     for j in range(5):#inner for loop
#         print(i,j)


# for i in range(1,6):#outer for loop
#     for j in range(1,11): #inner for loop
#         print(f"{i} X {j} = {i*j}")
#     print()


#syntax while
# while True:
#     #block of code


# while True:
#     print("welcome to pythonlife")



# count = 0
# while count<3:
#     print(count)
#     count +=1



# while True:
#     user_name = input("enter username: ")
#     password = input("enter the password: ")
#     if user_name == "durga" and password == "durga@123":
#         print("login successfull")
#         break
#     else:
#         print("invalid credentials")


#while cond:#outer while
    #while cond:#inner while 


# outer = 0
# while outer<2:
#     inner = 0
#     while inner<2:
#         print(outer,inner)
#         inner +=1
#     outer+=1



# while True:
    # print("pythonlife")
    # print("welcome to pythonlife")
    # while True:
    #     print("hello everyone, welcome to pythonlife")
    #     break

sum = 0
for i in range(1,6):
    result = i**2
    sum+=result
print(f"sum of square {sum}")