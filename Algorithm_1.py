# # TODO: Homework: Rewrite a program with any number of digits.
# #  Instead of  3 digits, you should sum digits up from n digits number,
# #  Where  User enters n manually. n > 0
#
# from random import randint
#
# n = int(input('Enter digit number '))
# a = randint(10**(n-1), 10**n-1)
# print(a)
# summ = 0
# while n > 0:
#     b = a % 10
#     summ = summ + b
#     n = n - 1
#     a = a // 10
#
# print(summ)
#
#
# # Find max number from 3 values, entered manually from a keyboard
#
# a = int(input('Enter value N1: '))
# b = int(input('Enter value N2: '))
# c = int(input('Enter value N3: '))
#
# if a > b:
#     if a > c:
#         print(f'Max value is {a}')
#     elif c > a:
#         print(f'Max value is {c}')
# elif a == b:
#     if c > a:
#         print(f'Max value is {c}')
#     elif a > c:
#         print(f'Max value is {a}')
#     elif a == b:
#         print('All values are equal')
# elif a < b:
#     if b > c:
#         print(f'Max value is {a}')
#     elif b > a:
#         print(f'Max value is {c}')
#
#
# # Count odd and even numbers.
# # Count odd and even digits of the whole number.
# # E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).
#
#
# numb = input('Enter the number: ')
# n = len(numb)
# numb_1 = int(numb)
# odd = 0
# even = 0
# a = 0
# while n > 0:
#     a = numb_1 % 10
#     if a % 2 == 0:
#         even += 1
#     elif a % 2 != 0:
#         odd += 1
#     numb_1 = numb_1 // 10
#     n = n - 1
#
# print(f'{odd} digit(s) is (are) odd')
# print(f'{even} digit(s) is (are) even')
#
#
# # from codewars:
# # Create a method sayHello/say_hello/SayHello
# # that takes as input a name, city, and state to welcome a person.
# # Note that name will be an array consisting of one or more values
# # that should be joined together with one space betweeen each,
# # and the length of the name array in test cases will vary.
# # import string
# # from string import join
#
# def say_hello(name, city, state):
#     str1 = ' '.join(name)
#     print(f'Hello, {str1}! Welcome to {city}, {state}!')
# #
# #
# #
# #
# say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
#
#
# # Digital root is the recursive sum of all the digits in a number.
#
# # Given n, take the sum of the digits of n.
# # If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# # This is only applicable to the natural numbers.
#
# # 16  -->  1 + 6 = 7
# # 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
#
# def digital_root(n):
#     a = len(str(n))
#     summ = 0
#     b = 0
#     while a > 0:
#         b = n % 10
#         summ = summ + b
#         n = n // 10
#         a = a - 1
#     if summ > 9:
#         digital_root(summ)
#     else:
#         return summ


print(digital_root(942))