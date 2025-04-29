# tuple_1 = ()
# print(type(tuple_1))

# tuple_2 = (1,2,5.7,"sai",True,(1,2),{1,2},{1:1},1,11,1,1,1)
# print(type(tuple_2))

# tuple_3 = tuple()
# print(type(tuple_3))

# tuple_2 = (1,2,5.7,"sai",True,(1,2),{1,2},{1:1},1,11,1,1,1)
# print(len(tuple_2))

# numbers = (1, 2, 3, 1, 4, 1)
# print(numbers.count(1))
# print(numbers.index(1))

# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# result_tuple = tuple1 + tuple2
# print(result_tuple)
# print(tuple1*3)


# fruits = ('apple', 'banana', 'orange')
# print("3" in fruits)


# numbers = ()
# print(all(numbers))


# numbers = (1, 2, 3, 1, 4, 1)
# print(numbers[2])
# print(numbers[-4])
# print(numbers[1:4])
# print(numbers[-5:-2])
# print(numbers[::-1])


items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
sum = 0
print(f"Item		Price")
print("-"*20)
for i,j in items:
    print(i,j)