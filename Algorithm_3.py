"""

Write a Python function, which will count how many times a character
(substring) is included in a string. DON’T USE METHOD COUNT


"""

txt1 = input('Enter the string: ')
char1 = input('Enter character: ')

def count_me(txt, char):
    counter = 0
    for char in txt:
        if char == char1:
            counter += 1
    return counter


print(count_me(txt1, char1))


# For substring:

txt1 = input('Enter the string: ')
sub1 = input('Enter substring: ')

def count_me_2(txt, sub):
    counter = 0
    for i, c in enumerate(txt):
        if sub == txt[i:i + len(sub)]:
            counter += 1
    return counter


print(count_me_2(txt1, sub1))




"""

Find and replace a substring in a string for another substring. 
User enter from a keyboard a string and both substrings. 
DON’T USE METHOD REPLACE

"""

txt = input('Enter string: ')
sub1 = input('Enter substring 1: ')
sub2 = input('Enter substring 2: ')

def sub_on_sub(text, substr1, substr2):
    i = text.find(substr1)
    l = len(substr1)
    return text[0:i]+substr2+text[i+l:-1]

print(sub_on_sub(txt, sub1, sub2))

"""
TODO: Write a function for decompressing string “a4b3c2d”

"""


def decompression(str):
    newstr = ''
    for a in str:
        if a.isdigit() == True:
            newstr += newstr[-1] * (int(a)-1)
        elif a.isdigit() == False:
            newstr += a
    return newstr




print(decompression('a4b3c2d'))

#  Tasks from Codewars:


"""
You will be given an array a and a value x. 
All you need to do is check whether the provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not.

"""
def check(seq, elem):
    return elem in seq

print(check([66, 101], 55))


"""
You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.

"""

def positive_sum(arr):
    l = len(arr)
    s = 0
    while l > 0:
        if arr[l-1] > 0:
            s += arr[l-1]
            l -= 1
        else:
            l -= 1
    return s

def positive_sum(arr):
    s =0
    for i in arr:
        if i > 0:
            s += i
    return s



print(positive_sum([1,-2,3,4,5]))


def digitize(n):
    l = (list(map(int, str(n))))
    l.reverse()
    return l



"""
Write a function that reverses the bits in an integer.
For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.
You can assume that the number is not negative.

"""
import reverse
n = 35
a = format(n, 'b')
l = list(map(str, a))
l.reverse()
s2 = ''.join(l)
b = int(s2, 2)
print(b)


"""
Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string, 
and produces outputs according to the following table:

Input	Output
"Jabroni"	"Patron Tequila"
"School Counselor"	"Anything with Alcohol"
"Programmer"	 "Hipster Craft Beer"
"Bike Gang Member"	"Moonshine" 
"Politician"	"Your tax dollars" 
"Rapper"	"Cristal"  
*anything else*	"Beer" 
Note: anything else is the default case: if the input to the function is not any of the values in the table, 
then the return value should be "Beer."

Make sure you cover the cases where certain words do not show up with correct capitalization. 
For example, getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".


"""

def get_drink_by_profession(param):
    a = {
        "jabroni": "Patron Tequila",
        "school Counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike Gang Member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    if param in a:
        return a[param.lower()]
    else:
        return "Bear"

print(get_drink_by_profession("ddd"))


