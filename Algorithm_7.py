"""
Selection sort

"""
from random import randint


def selection_sort(array):
    for i, _ in enumerate(array):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

# It is more understandable for me (I don't understand enumerate):
    for i in range(len(array)):
        min_ind = i
        for j in range(i+1, len(array)):
            if array[min_ind] > array[j]:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]
    return array


n = 5
unsorted_list = []
for _ in range(n):
    unsorted_list.append(randint(1, 99))

print(f'input: {unsorted_list}')
print(f'output: {selection_sort(unsorted_list)}')


"""
Bubble sort

"""


def bubble_sort(l):
    for i in range(len(l)):
        j = len(l)-1
        while j > 0:
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l


n = 5
unsorted_list = []
for _ in range(n):
    unsorted_list.append(randint(1, 99))

print(f'input: {unsorted_list}')
print(f'output: {bubble_sort(unsorted_list)}')


"""
Insertion Sort

"""


def insertion_sort(l):
    for i in range(len(l)):
        temp = l[i]
        j = i - 1
        while j >= 0 and temp < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = temp
    return l


n = 5
unsorted_list = []
for _ in range(n):
    unsorted_list.append(randint(1, 99))

print(f'input: {unsorted_list}')
print(f'output: {insertion_sort(unsorted_list)}')


"""
Selection sort with Key
"""


def selection_sort(array):
    for i in range(len(array)):
        min_ind = i
        for j in range(i+1, len(array)):
            if array[min_ind]['age'] > array[j]['age']:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]
    return array


unsorted_list = [
    {
        'name': 'Andrei',
        'age': 34
    },
    {
        'name': 'Ilya',
        'age': 25
    },
    {
        'name': 'Olga',
        'age': 28
    }
]

print(f'input: {unsorted_list}')
print(f'output: {selection_sort(unsorted_list)}')


"""
Bubble sort with key
"""


def bubble_sort(l):
    for i in range(len(l)):
        j = len(l)-1
        while j > 0:
            if l[j]['age'] < l[j-1]['age']:
                l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l


unsorted_list = [
    {
        'name': 'Andrei',
        'age': 34
    },
    {
        'name': 'Ilya',
        'age': 25
    },
    {
        'name': 'Olga',
        'age': 29
    }
]

print(f'input: {unsorted_list}')
print(f'output: {bubble_sort(unsorted_list)}')


"""
Insertion Sort
"""


def insertion_sort(l):
    for i in range(len(l)):
        temp = l[i]
        j = i - 1
        while j >= 0 and temp['age'] < l[j]['age']:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = temp
    return l


unsorted_list = [
    {
        'name': 'Andrei',
        'age': 34
    },
    {
        'name': 'Ilya',
        'age': 25
    },
    {
        'name': 'Olga',
        'age': 29
    }
]

print(f'input: {unsorted_list}')
print(f'output: {insertion_sort(unsorted_list)}')


"""
Tasks from Codewars.com
"""


# 1:

"""
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters 
and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!
"""


def solve(s):
    counter = 0
    for i in s:
        if i.islower():
            counter += 1
    print(counter)
    if counter >= len(s)/2:
        return s.lower()
    else:
        return s.upper()


print(solve("code"))


# 2:

"""
Take an input string and return a string that is made up of the number 
of occurences of each english letter in the input followed by that letter, sorted alphabetically. 
The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

the input will always be valid;
treat letters as case-insensitive
Examples
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
"""


def string_letter_count(s):
    s = s.lower()
    counter = 0
    res = ''
    for item in sorted(s.lower()):
        if item.isalpha():
            counter = s.count(item)
            if item not in res:
                res += str(counter)+item
    return res


print(string_letter_count("The quick brown fox jumps over the lazy dog."))
