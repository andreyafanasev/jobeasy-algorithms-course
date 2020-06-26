"""
# 1 Enter a string of words separated by spaces. Find the longest word.

"""

def long_word(string):
    counter = 0
    list1 = string.split()
    l = len(list1)
    while l > 0:
        if counter < len(list1[l-1]):
            counter = len(list1[l-1])
            l -= 1
        else:
            l -= 1
    return counter

print(long_word('Find the longest word'))



"""
# 2 Enter an irregular string (that means it may have space at the beginning of a string, 
at the end of the string, and words may be separated by several spaces). 
Make the string regular (delete all spaces at the beginning and end of the string, leave one space separating words).

"""

def irreg_str(string):
    l = string.split()
    return ' '.join(l)



print(irreg_str('  Find    the    longest    word  '))


"""
From Codewars # 1
Define String.prototype.toAlternatingCase 
(or a similar function/method such as to_alternating_case/toAlternatingCase
/ToAlternatingCase in your selected language; 
see the initial solution for details) such that each lowercase letter becomes uppercase 
and each uppercase letter becomes lowercase. For example:

hEllO wOrld
"""

def to_alternating_case(string):
    result = ''
    for i in string:
        if i.islower() == True:
            result += i.upper()
        else:
            result += i.lower()
    return result

print(to_alternating_case("1a2b3c4d5e"))



"""
From Codewars # 2

Is the string uppercase?
Task
Create a method is_uppercase() to see whether the string is ALL CAPS. For example:

is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter 
so any string containing no letters at all is trivially considered to be in ALL CAPS.



"""

def is_uppercase(inp):
    return inp.isupper()

print(is_uppercase('ACSKLDFJSgSKLDFJSKLDFJ'))



"""
From Codewars # 3

Given a string of digits, you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string.

"""
def fake_bin(x):
    res = ''
    l = list(x)
    for i in l:
        if int(i) < 5:
            res += '0'
        else:
            res += '1'
    return res

print(fake_bin("1234888"))