# dict_1 = {
# }
# print(type(dict_1))


# dict_2 = dict()
# print(type(dict_2))


# emp_data = {
#     1:"vasu",
#     2:"hemasai",
#     3:"poojitha",
#     4:"karthik",
#     5:{1:"vas1u"},
#     (1,2):"it was tuple",
#     "user1": "user1@123",
# }
# print(emp_data)

# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1.clear()
# copy_dict= dictionary_1.copy()
# print(dictionary_1.get("user5"))
# print(dictionary_1["user5"])

# list_1 = [1,2,3,4]
# print(list_1[2])


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1.items())
# print(dictionary_1.keys())
# print(dictionary_1.values())
# obj = dictionary_1.pop("user4")
# print(obj)
# print(dictionary_1)




# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }

# dictionary_2 ={
#     "user5":"user5@123",
#     1:1234,
#     2:2345,
#     3:4567,
# }

# dictionary_1.update(dictionary_2)
# print(dictionary_1)
# print(dictionary_2)










# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# #var[key] = value
# dictionary_1["user4"] = "user4@123456" #changing
# dictionary_1["user5"] = "user5@1234" #adding
# print(dictionary_1)




# dictionary_1 ={

# }
# dictionary_1[1] = 1234
# dictionary_1[2] = 12345
# print(dictionary_1)



user_data = {}

username = input("enter the username: ")
password = input("enter the password: ")
user_data[username] = password
print(user_data)