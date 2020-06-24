# TODO HW: Rewrite code, which will return only needed element of Fib sequence


n = int(input('Enter number of elements of Fib sequence '))
fib_1 = 1
fib_2 = 1

if n == 0:
    print(1)
if n > 0:
    print(fib_1)
if n > 1:
    print(fib_2)
    index = 0
    while index < n-2:
        fib_1, fib_2 = fib_2, fib_1+fib_2
        index += 1
        print(fib_2)



# TODO Use datetime library to solve problem Seconds to Date

from datetime import timedelta

sec = int(input('Enter seconds: '))
print(timedelta(seconds = sec))

# TODO Zeros not for Heros
#  Numbers ending with zeros are boring.
#  They might be fun in your world, but not here.
#  Get rid of them. Only the ending ones.
#  1450 -> 145
#  960000 -> 96
#  1050 -> 105
#  -1050 -> -105
#  Zero alone is fine, don't worry about it. Poor guy anyway


def hero(n):
    while n % 10 == 0:
        n = n // 10
    print(n)

hero(-1050)

# TODO Digital root is the recursive sum of all the digits in a number.
#  Given n, take the sum of the digits of n.
#  If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
#  This is only applicable to the natural numbers.
#  16  -->  1 + 6 = 7
#  942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#  132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#  493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# I fixed this code!!!! Now it works!!

def digital_root(n):
    while n > 9:
        l = len(str(n))
        num_1 = n
        summ = 0
        while l > 0:
            summ = summ + num_1 % 10
            l -= 1
            num_1 = num_1 // 10
        n = summ
    else:
        return n

print(digital_root(132189))






# TODO Task from Codewars #1
#  Complete the function which get an input number n such that n >= 10 and n < 10000, then:
#  Sum all the digits of n.
#  Subtract the sum from n, and it is your new n.
#  If the new n is in the list below return the associated fruit, otherwise return back to task 1.
#  Example
#  n = 325
#  sum = 3+2+5 = 10
#  n = 325-10 = 315 (not in the list)
#  sum = 3+1+5 = 9
#  n = 315-9 = 306 (not in the list)
#  sum = 3+0+6 = 9
#  n =306-9 = 297 (not in the list)
#  . .
#  . ...until you find the first n in the list below.


def subtract_sum(number):
    a = {1: 'kiwi', 2: 'pear', 3: 'kiwi', 4: 'banana', 5: 'melon', 6: 'banana', 7: 'melon', 8: 'pineapple', 9: 'apple',
10: 'pineapple', 11: 'cucumber', 12: 'pineapple', 13: 'cucumber', 14: 'orange', 15: 'grape', 16: 'orange',17: 'grape',
18: 'apple', 19: 'grape', 20: 'cherry', 21: 'pear', 22: 'cherry', 23: 'pear', 24: 'kiwi', 25: 'banana', 26: 'kiwi',
27: 'apple', 28: 'melon', 29: 'banana', 30: 'melon', 31: 'pineapple', 32: 'melon', 33: 'pineapple', 34: 'cucumber',
35: 'orange', 36: 'apple', 37: 'orange', 38: 'grape', 39: 'orange', 40: 'grape', 41: 'cherry', 42: 'pear', 43: 'cherry',
44: 'pear', 45: 'apple', 46: 'pear', 47: 'kiwi', 48: 'banana', 49: 'kiwi', 50: 'banana', 51: 'melon', 52: 'pineapple',
53: 'melon', 54: 'apple', 55: 'cucumber', 56: 'pineapple', 57: 'cucumber', 58: 'orange', 59: 'cucumber', 60: 'orange',
61: 'grape', 62: 'cherry', 63: 'apple', 64: 'cherry', 65: 'pear', 66: 'cherry', 67: 'pear', 68: 'kiwi', 69: 'pear',
70: 'kiwi', 71: 'banana', 72: 'apple', 73: 'banana', 74: 'melon', 75: 'pineapple', 76: 'melon', 77: 'pineapple',
78: 'cucumber', 79: 'pineapple', 80: 'cucumber', 81: 'apple', 82: 'grape', 83: 'orange', 84: 'grape', 85: 'cherry',
86: 'grape', 87: 'cherry', 88: 'pear', 89: 'cherry', 90: 'apple', 91: 'kiwi', 92: 'banana', 93: 'kiwi', 94: 'banana',
95: 'melon', 96: 'banana', 97: 'melon', 98: 'pineapple', 99: 'apple', 100: 'pineapple'}
    while number > 100:
        l = len(str(number))
        num_1 = number
        summ = 0
        while l > 0:
            summ = summ + num_1 % 10
            l -= 1
            num_1 = num_1 // 10
        number = number - summ
    else:
        return a[number]


print(subtract_sum(110))




# TODO Task frome codewars #2
#  This function takes two numbers as parameters, the first number being the coefficient,
#  and the second number being the exponent.
#  Your function should multiply the two numbers, and then subtract 1 from the exponent.
#  Then, it has to print out an expression (like 28x^7). "^1" should not be truncated when exponent = 2.
#  For example:
#  derive(7, 8)
#  In this case, the function should multiply 7 and 8, and then subtract 1 from 8.
#  It should output "56x^7", the first number 56 being the product of the two numbers,
#  and the second number being the exponent minus 1.
#  derive(7, 8) --> this should output "56x^7"
#  derive(5, 9) --> this should output "45x^8"
#  Notes:
#  The output of this function should be a string
#  The exponent will never be 1, and neither number will ever be 0

def derive(coefficient, exponent):
    return f'{coefficient * exponent}x^{exponent - 1}'


print(derive(7, 8))


# TODO Task from Codewars #3
#  Step 1: Create a function called encode() to replace all the lowercase vowels in a given string
#  with numbers according to the following pattern:
#  a -> 1
#  e -> 2
#  i -> 3
#  o -> 4
#  u -> 5
#  For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
#  Step 2: Now create a function called decode()
#  to turn the numbers back into vowels according to the same pattern shown above.
#  For example, decode("h3 th2r2") would return "hi there".
#  For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


def encode(st):
    return st.replace('a', '1').replace('e', '2').replace('i', '3').replace('o', '4').replace('u', '5')

print(encode("hello"))

def decode(st):
    return st.replace('1', 'a').replace('2', 'e').replace('3', 'i').replace('4', 'o').replace('5', 'u')

print(decode("h3 th2r2"))



# TODO Task from Codewars #4
#  Given three integers a ,b ,c, return the largest number obtained after inserting
#  the following operators and brackets: +, *, ()
#  In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained
#  Consider an Example :
#  With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:
#  1 * (2 + 3) = 5
#  1 * 2 * 3 = 6
#  1 + 2 * 3 = 7
#  (1 + 2) * 3 = 9
#  So the maximum value that you can obtain is 9.
#  Notes
#  The numbers are always positive.
#  The numbers are in the range (1  ≤  a, b, c  ≤  10).
#  You can use the same operation more than once.
#  It's not necessary to place all the signs and brackets.
#  Repetition in numbers may occur .
#  You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.



def expression_matter(a, b, c):
    return max(a+b+c, a*b*c, (a+b)*c, a*(b+c))

print(expression_matter(5,1,3))


# TODO Task from Codewars #5
#  Our football team finished the championship. The result of each match look like "x:y".
#  Results of all matches are recorded in the collection.
#  For example: ["3:1", "2:2", "0:1", ...]
#  Write a function that takes such collection and counts the points of our team in the championship.
#  Rules for counting points for each match:
#  if x>y - 3 points
#  if x<y - 0 point
#  if x=y - 1 point
#  Notes:
#  there are 10 matches in the championship
#  0 <= x <= 4
#  0 <= y <= 4


def points(games):
    n = len(games)-1
    p = 0
    while n >= 0:
        x = list(games[n])[0]
        y = list(games[n])[-1]
        n -= 1
        if x > y:
            p += 3
        elif x == y:
            p += 1
        else:
            p = p
    return p

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))


n1 = int(input('Enter number of elements of Fib sequence '))


# TODO HW: Rewrite code, which will return only needed element of Fib sequence.
# Fixed variant, from last class

def fib(n):
    fib_1 = 1
    fib_2 = 1
    if n > 1:
        index = 0
        while index < n-2:
            fib_1, fib_2 = fib_2, fib_1+fib_2
            index += 1
        return fib_2
    elif n == 1:
        return 1
    else:
        return 0


print(fib(n1))