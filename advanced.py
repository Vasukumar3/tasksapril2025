# lambda arguments: expression

# def add(a,b):# function definition
#     return a+b #
# print(add(10,10))

#syntax
# lambda arguments: expression
# result = lambda a,b: a+b
# print(result(10,10))


# result = lambda a,b,c: a+b+c
# print(result(10,20,50))

# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24]
# empty_list = []
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)


#syntax
# filter(function, iterable)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24]
# def even(a):
#     return a%2==0
# obj = filter(even,list_1)
# print(list(obj))


#lambda arg:exp
#filter(func,iter)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# result = filter(lambda a:a%2==0,list_1)
# print(list(result))


# Syntax:
# map(function, iterable, ...)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# empty_list= []
# for i in list_1:
#     result = i**2
#     empty_list.append(result)
# print(empty_list)


# map(fun,iterab,...)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# def square(a):
#     return a**2
# result = map(square,list_1)
# print(list(result))


#lambda arg:exp
#map(func,iter,..)
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# # list_2 =[25,45,22,58,96,10,58,1,2,36,79,24,2]
# result = map(lambda a:a**2,list_1)
# print(list(result))


# Syntax:
# from functools import reduce
# reduce(function, iterable[, initializer])#initializer--optional



# from functools import reduce
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# def add(a,b):
#     return a+b
# result = reduce(add,list_1)
# print(result)


# from functools import reduce
# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# result = reduce(lambda a,b:a+b,[10,20,30,40,50])
# print(result)


# list_1 = [25,45,22,58,96,10,58,1,2,36,79,24,24]
# maximum = list_1[0]
# for i in list_1:
#     if i > maximum:
#         maximum = i
# print(maximum)

# def maximum(a):
#     return max(a)
# print(maximum([25,45,22,58,96,10,58,1,2,36,79,24,24]))

# from functools import reduce
# result = reduce(lambda a,b:a if a>b else b,  [25,45,22,58,96,10,58,1,2,36,79,24,24])
# print(result)


"""
generator function --  a genetor -function is defined like a normal function
but whenever its need to generate a value
it does so with the yeild keyword rather than return
if body contain yield , the function  automatically
becomes a generator function.
"""

# def sample():
#     yield 1 #pause or hold
#     yield 2 #pause or hold
#     yield 3 #pause or hold
# obj = sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
