# 1. Reverse a String

# Input:  "hello"
# Output: "olleh"

def reverse_string(s):
    output = ""
    for i in range(len(s)-1,-1,-1):
        output+= s[i]

    return output

result = reverse_string("gokul")
print(result)

# Python also has:
# s[::-1]


# Problem 2 — Palindrome:

# Input:  "madam"
# Output: True

# Input:  "hello"
# Output: False

def is_palindrome(s):
    output = ""
    for i in range(len(s)-1,-1,-1):
        output+= s[i]

    return output == s

result = is_palindrome(s="madam")
print(result)

# Problem 3 — Count Vowels.
# Input:  "programming"
# Output: 3

def count_vowels(s):
    vowels = {"a","e","i","o","u"}

    output = 0

    for i in s:
        if i.lower() in vowels:
            output += 1

    return output


result = count_vowels(s="HELLO")
print(result)


# Problem 4 — Find Largest Number

# input: numbers = [10, 4, 25, 7, 18]
# output: 25

def find_largest(numbers):
    output = numbers[0]

    for i in numbers:
        if i > output:
            output = i

    return output


result = find_largest(numbers=[10, 4, 25, 7, 18])
print(result)


# Problem 5 — Count Occurrences

# Given a list of numbers and a target number, count how many times the target appears.

# Input
# numbers = [1, 2, 3, 2, 4, 2, 5]
# target = 2

# output = 3

def count_occurrences(numbers, target):
    counter = 0

    for i in numbers:
        if i == target:
            counter+=1

    return counter

result = count_occurrences(numbers=[10, 20, 10, 30, 10,10,10],target=10)
print(result)



# Problem 6 - Remove Duplicates
# Given:
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# Output:
# [1, 2, 3, 4, 5]

def remove_duplicates(numbers):
    output = []
    for i in numbers:
        if i not in output:
            output.append(i)

    return output
            

result = remove_duplicates(numbers= [1, 2, 2, 3, 4, 4, 5, 5, 5])
print(result)


# Problem 7 — Find Second Largest Number
# Given:
# numbers = [10, 4, 25, 7, 18]
# output:
# 18

def find_second_largest(numbers):
    first_largest = numbers[0]

    second_largest = None

    for i in numbers:
        if i > first_largest:
            first_largest = i

    for i in numbers:
        if i < first_largest:
            if second_largest is None or i > second_largest:
                second_largest = i


    return second_largest
   
result = find_second_largest(numbers = [10, 4, 25, 7, 18])
print(result)


# Problem 8 — Find Even Numbers
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected =  [2, 4, 6, 8]

def find_even_numbers(numbers):
    output = []
    for i in numbers:
        if i % 2 == 0:
            output.append(i)

    return output

result = find_even_numbers(numbers= [1, 2, 3, 4, 5, 6, 7, 8])
print(result)


# Problem 9 — Sum of List
# Given:
# numbers = [10, 20, 30, 40, 50]
# expected: 150

def calculate_sum(numbers):
    output = 0
    for i in numbers:
        output+= i
    return output

result = calculate_sum(numbers= [10,20,30,40,50])
print(result)


# Problem 10 — Find Common Elements

# Given two lists:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# output:
# [3, 4, 5]


def find_common(list1, list2):
    output = []

    for i in list1:
        for j in list2:
            if i == j:
                output.append(i)

    return output


result = find_common(list1 = [1, 2, 3, 4, 5],list2 = [3, 4, 5, 6, 7])
print(result)


# Problem 11 — Reverse a List

def reverse_list(numbers):
    output = []
    for i in range(len(numbers)-1,-1,-1):
        output.append(numbers[i])

    return output

result = reverse_list(numbers = [1, 2, 3, 4, 5])
print(result)



# Problem 12 — Count Even and Odd Numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# output:
# Even: 4
# Odd: 4

def count_even_odd(numbers):
    even = 0
    odd  = 0
    for i in numbers:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    
    return even,odd

result = count_even_odd(numbers=[1, 2, 3, 4, 5, 6, 7, 8])
print(result)




# Problem 14 — Find the Frequency of Each Element

# This is a very important interview pattern because it introduces dictionaries.

# Given:
# numbers = [1, 2, 2, 3, 1, 2, 4, 3]

# Expected:
# {
#     1: 2,
#     2: 3,
#     3: 2,
#     4: 1
# }


def count_frequency(numbers):
    output = {}

    for i in numbers:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1

    return output


result = count_frequency(numbers=[1, 2, 2, 3, 1, 2, 4, 3])
print(result)


#  Problem 15 — First Non-Repeating Character

# Given:
# s = "aabbcdde"

# Expected output:
# c

# Because:
# a → 2 times
# b → 2 times
# c → 1 time  ← first non-repeating
# d → 2 times
# e → 1 time


def first_non_repeating(s):
    output = {}

    for i in s:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1

    for j in s:
        if output[j] == 1:
            return j

    return None


result = first_non_repeating(s="aabbcdde")
print(result)