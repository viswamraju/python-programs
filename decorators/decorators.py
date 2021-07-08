#
# How decorator works.  Basic

# def f1():
#     print("Say Hello")
#
#
# def f2(func):
#     print("Start")
#     func()
#     print("end")
#
#
# f2(f1)

# Decorators with arguments
#
# def f2(func):
#     def wrapper(*args, **kwargs):
#         print("start")
#         func(*args, **kwargs)
#         print("end")
#     return wrapper
#
#
# @f2
# def f1(name):
#     print("Hello ", name)
#
# f1("viswam")

# Return from decorator

# def f2(func):
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args)
#         print("end")
#         return result
#     return wrapper
#
#
# @f2
# def add(a, b):
#     return a + b
#
# print(add(1, 2))


# Decorator with params

# def f2(*args, **kwargs):
#     def wrapper(func):
#         def inner(*args1, **kwarg1):
#             print("strat")
#             print(args)
#             func()
#             print(args1)
#             print("end")
#         return inner
#     return wrapper
#
#
# def f1():
#     print("Hello")
#
#
# f2(1, 2)(f1)(3, 4)


# Multi decorators

# def deco1(func):
#     def wrapper():
#         print("start deco1")
#         func()
#         print("end deco1")
#     return wrapper
#
#
# def deco2(func):
#     def wrapper():
#         print("start deco2")
#         func()
#         print("end deco2")
#     return wrapper
#
#
# @deco2
# @deco1
# def f1():
#     print("hello")
#
#
# def f2():
#     print("hello")
#
#
# f1()
#
# print("-------")
# deco2(deco1(f2))()
