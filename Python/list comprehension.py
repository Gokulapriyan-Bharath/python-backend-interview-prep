# List Comprehension in Python

"""

List Comprehension in Python

A list comprehension is a concise way to create a new list from an iterable, optionally applying a condition or transformation.

The basic syntax is:

[expression for item in iterable]
1. Normal for Loop

Suppose we want squares:

numbers = [1, 2, 3, 4, 5]


squares = []


for number in numbers:
    squares.append(number * number)


print(squares)

Output:

[1, 4, 9, 16, 25]
2. Same Thing Using List Comprehension
numbers = [1, 2, 3, 4, 5]


squares = [number * number for number in numbers]


print(squares)

Output:

[1, 4, 9, 16, 25]

So:

for loop
→ multiple lines


list comprehension
→ concise expression
3. With a Condition

Suppose we only want even numbers.

Normal loop:
numbers = [1, 2, 3, 4, 5, 6]


even_numbers = []


for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)


print(even_numbers)

Output:

[2, 4, 6]
List comprehension:
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]


print(even_numbers)

Output:

[2, 4, 6]

The syntax is:

[expression for item in iterable if condition]
4. Transformation vs Filtering

This is an important distinction.

Transformation
numbers = [1, 2, 3]


squares = [x * x for x in numbers]

You're transforming each value.

Result:

[1, 4, 9]
Filtering
numbers = [1, 2, 3, 4]


even = [x for x in numbers if x % 2 == 0]

You're filtering values.

Result:

[2, 4]
5. Real Backend Example

Suppose you have users:

users = [
    {"name": "Gokul", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Arun", "active": True}
]

You want the names of active users:

active_users = [
    user["name"]
    for user in users
    if user["active"]
]


print(active_users)

Output:

['Gokul', 'Arun']

This type of data transformation is common when processing API responses.

6. Nested List Comprehension

You can have nested loops:

matrix = [
    [1, 2],
    [3, 4]
]


result = [
    number
    for row in matrix
    for number in row
]


print(result)

Output:

[1, 2, 3, 4]

Equivalent normal loops:

result = []


for row in matrix:
    for number in row:
        result.append(number)

But be careful: don't make comprehensions unnecessarily complicated. Readability matters in production code.

7. List Comprehension vs Generator Expression

This is a common follow-up.

List comprehension:

numbers = [x * x for x in range(1000000)]

creates the entire list in memory.

Generator expression:

numbers = (x * x for x in range(1000000))

produces values lazily as you iterate.

So:

List comprehension
→ creates list immediately
→ more memory


Generator
→ lazy evaluation
→ less memory

We'll cover generators separately because they're an important Python interview topic.

8. Interview-Ready Answer

If they ask:

What is a list comprehension?

Say:

"A list comprehension is a concise way to create a list from an iterable. It can optionally include a condition for filtering. For example, [x * x for x in numbers] creates a list of squares. It's generally more concise than a traditional loop, but I avoid using overly complex comprehensions because readability is important."

That's a good interview answer.

Quick Memory
[expression for item in iterable]

With condition:

[expression for item in iterable if condition]

Example:

[x * 2 for x in numbers if x > 5]
"""