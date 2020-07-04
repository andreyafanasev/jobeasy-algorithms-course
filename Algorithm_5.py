"""
HW 1. Last problem from slides (Sum of odd numbers)


Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

"""

def row_sum_odd_numbers(n):
    summ = 0
    d = n*(n-1)+1
    while n > 0:
        summ += d
        d += 2
        n -= 1
    return summ
# Or that i found later:
# and it is so easy
def row_sum_odd_numbers(n):
    return n**3


print(row_sum_odd_numbers(3))

"""
When given a list, the program should return a list of all the elements that are below 
the arithmetical mean of the original list.  
The arithmetical mean is the sum of all elements divided by the number of elements.


"""

def below_the_arithmetical_mean(l):
    nlist = []
    for item in l:
        if item < sum(l)/len(l):
            nlist.append(item)
    return nlist


print(below_the_arithmetical_mean([1,2,3,4,5,6,7,8,9]))


"""
When given a list of elements find the two lowest elements. They can be equal to each other or different.  
"""

def two_lowest_elements(l):
    low1 = l[1]
    low2 = l[1]
    for i in range(len(l)):
        if l[i] <= low1:
            low1 = l[i]
    l.remove(low1)
    for i in range(len(l)):
        if l[i] <= low2:
            low2 = l[i]
    return [low1,low2]

print(two_lowest_elements([1,2,3,-2,-5,-1,90,-5]))




# codewars.com (3-4 problems)

"""
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


"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""


def duplicate_count(text):
    counter = 0
    dupl = ''
    for i in range(len(text)):
        if text.lower()[i] in text.lower().replace(text[i],'',1) and text.lower()[i] not in dupl:
            counter += 1
            dupl += text.lower()[i]
    return counter

print(duplicate_count("abba"))


"""
All Star Code Challenge #18

Create a function called that accepts 2 string arguments and returns 
an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

strCount('Hello', 'o') // => 1
strCount('Hello', 'l') // => 2
strCount('', 'z')      // => 0
Notes:

The first argument can be an empty string
The second string argument will always be of length 1
"""

def str_count(strng, letter):
    counter = 0
    for i in range(len(strng)):
        if strng[i] == letter:
            counter += 1
    return counter