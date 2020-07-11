"""
Write a recursive function to count all the elements in a list (divide and rule).

"""
l1 = [1,2,3,4,5,'a',11]
def count(l: list):
    counter = 0
    if len(l) == 0:
        return 0
    else:
        counter += 1 + count(l[1:])
    return counter

print(count(l1))


"""
Find the biggest number in the list (divide and rule).

I wouldn't say that I understand it clear, that is complicated for me.

"""

def biggest(l, left, right):
    if len(l) == 0:
        return 0
    elif left == right:
        return l[left]
    else:
        mid = (left + right) // 2
        max1 = biggest(l, left, mid)
        max2 = biggest(l, mid + 1, right)
    return max1 if max1 > max2 else max2


print(biggest([1,2,3,4,5,4,3,1,10,12], 0, 9))


"""
Task from codewars #1:

You are going to be given an array of integers. 
Your job is to take that array and find an index N where the sum of 
the integers to the left of N is equal to the sum of the integers to the right of N. 
If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}: 
Your function will return the index 3, because at the 3rd position of the array, 
the sum of left side of the index ({1,2,3}) 
and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}: Your function will return the index 1, 
because at the 1st position of the array, 
the sum of left side of the index ({1}) 
and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index 
of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array 
can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal 
to the side to the right of N. If you do not find an index that fits these rules, 
then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.

"""

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    else:
        return -1

print(find_even_index([1,2,3,4,3,2,1]))


"""
Task from codewars #2:

A Narcissistic Number is a number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. 
In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:

Your code must return true or false depending upon whether the given number 
is a Narcissistic number in base 10.

Error checking for text strings or other invalid inputs is not required, 
only valid integers will be passed into the function.

"""

def narcissistic(value):
    summ = 0
    a = len(str(value))
    b = value
    c = a
    while a > 0:
        summ += (b % 10)**c
        b = b // 10
        a -= 1
    return summ == value


print(narcissistic(1634))

