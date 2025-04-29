#list --> mutable --> ordered elements
# list_1 = []
# print(type(list_1))


# list_2 = [1,2,5.7,"python",[1,2],1,2,5.7]
# print(type(list_2))

# list_3 = list()
# print(type(list_3))


# my_list = [10, 20, 30, 40, 50]
# #seq[index]
# print(my_list[2]) #30
# print(my_list[-3]) #30
# print(my_list[0]) #10
# print(my_list[-5]) #10
# print(my_list[4]) #50
# print(my_list[-1]) #50

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# #sequence[start:stop:step]
# print(my_list[1:4])
# print(my_list[0:4])
# print(my_list[0:8])
# print(my_list[3:7])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[4:7])
# print(my_list[-4:-1])
# print(my_list[-6:-2])

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[0:8:4])

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[0:8])
# print(my_list[:8])
# print(my_list[:])
# print(my_list[::])

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[::-1])
# print(my_list[5:2:-1])
# print(my_list[-3:-6:-1])




# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[:3])





################ april 12 2025 #####################
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# #syntax
# # .methodname(values)
# numbers.append(1234)
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.extend(["vasu","guru prasad","kiran",1,2,5.7,(1,2)])
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# copy_list = numbers.copy()
# copy_list.append("pythonlife")
# print(copy_list)
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.clear()
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers.count(10))

# numbers = [3, 4, 1, 5, 9, 2, 6, 5,1,1,1,1]
# print(numbers.index(1))


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,1,1,15,5,5,1]
# numbers.remove(1)
# print(numbers)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# obj = numbers.pop(4)
# obj1 = numbers.pop(-2)
# print(obj*5)
# print(obj1+25)
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.insert(5,"vasu")
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,[1,2,3]]
# print(len(numbers))


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.reverse()
# print(numbers)
# print(numbers[::-1])

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort(reverse=True)
# print(numbers)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][1])
# print(matrix[1][0])
# print(matrix[2][2])


# Syntax
# [expression for item in iterable]

# empty_list = []
# for i in range(1,6):
#     result = i**2
#     empty_list.append(result)
# print(empty_list)

# [exp for item in iterable]
# result = [i**2 for i in range(1,6)]
# print(result)

# print([i**2 for i in range(1,6)])

# empty_list = []
# for i in range(11):
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# # [exp for item in iterable if cond]
# result = [i for i in range(11) if i%2==0]
# print(result)

# print([i for i in range(11) if i%2==0])


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,1,1,15,5,5,1]
# empty_list = []
# for i in numbers:
#     if i!=1:
#         empty_list.append(i)
# print(empty_list)


# numbers = [3, 1, 4,[1,2,3,4],[1,2,3]]
# count = 0
# for item in numbers:
#     if item == 1:
#         count+=1
#     elif isinstance(item,list):
#         for subitem in item:
#             if subitem == 1:
#                 count+=1
# print(count)


# my_list = [10, 20, 30, 40, 50]
# print(my_list[1:4])

# print([x for x in range(11) if x % 2 == 0])