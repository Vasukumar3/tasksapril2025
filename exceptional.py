# types --> 3 types of errors
#1. syntax errors
#2. run time errors
#3. logical errors  --> user need to be identified (very difficult to find these errors)

#additional of two numbers
# num_1 = 10
# num_2 = 20
# result = num_1 - num_2
# print(result)


#1. syntax errors  --> are the compile time errors
# for i in range(11):
#     print(i)


# print(10+20)


#2. runtime errors ---> which disturbs the flow of execution ( during the execution ) also called exceptions

# num_1 = int(input("enter the number 1 "))
# num_2 = int(input("enter the number 2 "))
# print(num_1 + num_2)
# print(num_1 - num_2)
# try:
#     print(num_1 / num_2)
# except:
#     print("some error occured denominator should not be zero")
# else:
#     print(num_1 * num_2)
#     print(num_1 ** num_2)



# my_list = [10, 20, 30, 40]
# print(my_list[3])
# try:
#     print(my_list[5])
# except:
#     print("list index out of range")
# print(my_list[1])
# print(my_list[0])


# balance = 0

# def display_menu():
#     print("\nATM Menu:")
#     print("1. Credit")
#     print("2. Debit")
#     print("3. Balance")
#     print("4. Exit")

# def get_choice():
#     return input("Enter your choice (1-4): ")

# def credit():
#     global balance
#     try:
#         amount = float(input("Enter amount to credit: "))
#         if amount <= 0:
#             print("Please enter a positive amount.")
#         else:
#             balance += amount
#             print(f"${amount} credited to your account.")
#     except Exception as e:
#         print(e, "enter valid inputs")

# def debit():
#     global balance
#     try:
#         amount = float(input("Enter amount to debit: "))
#         if amount <= 0:
#             print("Please enter a positive amount.")
#         elif amount > balance:
#             print("Insufficient balance.")
#         else:
#             balance -= amount
#             print(f"${amount} debited from your account.")
#     except:
#         print("enter valid inputs 0-9 ")

# def show_balance():
#     print(f"Your current balance is: ${balance}")

# def main():
#     while True:
#         display_menu()
#         choice = get_choice()
        
#         if choice == '1':
#             credit()
#         elif choice == '2':
#             debit()
#         elif choice == '3':
#             show_balance()
#         elif choice == '4':
#             print("Thank you for using the ATM. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
# main()




# my_list = [10, 20, 30, 40]
# print(my_list[3])
# try:
#     print(my_list[10])
# except Exception as e:
#     print(e)
# else:
#     print(my_list[1])
#     print(my_list[0])
# finally:
#     print(my_list[10])









# try:
#     num_1 = int(input("enter the number: "))
#     num_2 = int(input("enter the number2: "))
# except Exception as e:
#     print(e)
# else:
#     print(num_1*num_2)


# num_1 = int(input("enter the number: "))
# num_2 = int(input("enter the number2: "))
# try:
#     print(num_1/num_2)
# except ZeroDivisionError as e:
#     print(e)



num_1 = int(input("enter the number: "))
num_2 = int(input("enter the number2: "))
try:
    print(num_1/num_2)
except ZeroDivisionError as e:
    print(e)