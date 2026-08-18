"""
append() vs extend() vs insert() in Python

These three methods modify a list, but they do it differently.

1. append()

append() adds one item to the end of the list.

numbers = [1, 2, 3]


numbers.append(4)


print(numbers)

Output:

[1, 2, 3, 4]
Important: append() adds the entire object as one element
numbers = [1, 2, 3]


numbers.append([4, 5])


print(numbers)

Output:

[1, 2, 3, [4, 5]]

The nested list is treated as one element.

2. extend()

extend() adds each element from an iterable to the end of the list.

numbers = [1, 2, 3]


numbers.extend([4, 5])


print(numbers)

Output:

[1, 2, 3, 4, 5]

Compare:

numbers = [1, 2, 3]
numbers.append([4, 5])


print(numbers)

Output:

[1, 2, 3, [4, 5]]

versus:

numbers = [1, 2, 3]
numbers.extend([4, 5])


print(numbers)

Output:

[1, 2, 3, 4, 5]
Easy memory trick

append() → adds one object
extend() → adds elements

3. insert()

insert() adds an element at a specific position.

Syntax:

list.insert(index, value)

Example:

numbers = [1, 2, 4]


numbers.insert(2, 3)


print(numbers)

Output:

[1, 2, 3, 4]

Here:

index:   0  1  2  3
value:  [1, 2, 3, 4]
4. Practical Comparison
numbers = [1, 2, 3]


numbers.append(4)
print(numbers)

Output:

[1, 2, 3, 4]

Then:

numbers.extend([5, 6])
print(numbers)

Output:

[1, 2, 3, 4, 5, 6]

Then:

numbers.insert(0, 100)
print(numbers)

Output:

[100, 1, 2, 3, 4, 5, 6]
5. Interview Trick

The interviewer might ask:

a = [1, 2]


a.append([3, 4])


print(a)

Output:

[1, 2, [3, 4]]

But:

a = [1, 2]


a.extend([3, 4])


print(a)

Output:

[1, 2, 3, 4]

This distinction is very important.

6. extend() Works With Any Iterable

It isn't limited to lists.

For example:

numbers = [1, 2]


numbers.extend((3, 4))


print(numbers)

Output:

[1, 2, 3, 4]

Even strings are iterable:

letters = ["a"]


letters.extend("bc")


print(letters)

Output:

['a', 'b', 'c']

But:

letters.append("bc")


print(letters)

Output:

['a', 'b', 'c', 'bc']

That's another nice interview trap.

7. Real-World Use Cases
append()

When you're adding one item:

users.append(new_user)
extend()

When you're combining collections:

all_users.extend(new_users)
insert()

When the position matters:

priority_tasks.insert(0, urgent_task)
8. Time Complexity

Generally:

append()  → O(1) amortized
extend()  → O(k), where k = number of elements added
insert()  → O(n)

Why is insert() O(n)?

Because when you insert near the beginning, existing elements need to be shifted.

For example:

Before:
[A, B, C, D]


insert X at index 0:


[X, A, B, C, D]

A, B, C, and D have to move.

9. Interview-Ready Answer

"append() adds a single object to the end of a list. extend() adds each element from an iterable to the end of the list. insert() adds an element at a specified index. For example, append([3,4]) creates a nested list, while extend([3,4]) adds 3 and 4 as separate elements."

Quick memory:
append(x)
→ Add x as ONE element


extend(x)
→ Add elements of x


insert(i, x)
→ Add x at index i

"""