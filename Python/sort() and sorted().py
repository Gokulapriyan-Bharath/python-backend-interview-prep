"""
sort() vs sorted() in Python

This is a very common interview question because it tests whether you understand in-place modification and return values.

1. sort()

sort() is a list method.

It modifies the original list in place.

numbers = [5, 2, 8, 1]


numbers.sort()


print(numbers)

Output:

[1, 2, 5, 8]

The original list has been changed.

2. sorted()

sorted() is a built-in Python function.

It returns a new sorted list and doesn't modify the original iterable.

numbers = [5, 2, 8, 1]


result = sorted(numbers)


print(result)
print(numbers)

Output:

[1, 2, 5, 8]
[5, 2, 8, 1]

So:

sort()
→ modifies original list


sorted()
→ creates and returns a new list
3. Very Common Interview Trap

The interviewer may ask:

numbers = [3, 1, 2]


result = numbers.sort()


print(result)

What is the output?

None

Why?

Because sort() sorts the list in place and returns None.

The list itself becomes:

[1, 2, 3]

So:

print(numbers)

gives:

[1, 2, 3]
4. sorted() Returns a Value
numbers = [3, 1, 2]


result = sorted(numbers)


print(result)

Output:

[1, 2, 3]

And the original remains:

print(numbers)

Output:

[3, 1, 2]
5. sorted() Works With More Than Lists

This is an important difference.

sort() only exists on lists:

numbers = [3, 1, 2]


numbers.sort()

But sorted() works with any iterable.

Tuple
numbers = (3, 1, 2)


result = sorted(numbers)


print(result)

Output:

[1, 2, 3]

Notice the result is a list, even though the input was a tuple.

Set
numbers = {3, 1, 2}


print(sorted(numbers))

Output:

[1, 2, 3]
6. Descending Order

Both support reverse=True.

numbers = [5, 2, 8, 1]


numbers.sort(reverse=True)


print(numbers)

Output:

[8, 5, 2, 1]

With sorted():

numbers = [5, 2, 8, 1]


result = sorted(numbers, reverse=True)


print(result)

Output:

[8, 5, 2, 1]
7. Sorting Using key

This is very useful in real backend code.

Suppose you have users:

users = [
    {"name": "Gokul", "age": 25},
    {"name": "Rahul", "age": 30},
    {"name": "Arun", "age": 22}
]

Sort by age:

users.sort(key=lambda user: user["age"])


print(users)

Result:

[
    {'name': 'Arun', 'age': 22},
    {'name': 'Gokul', 'age': 25},
    {'name': 'Rahul', 'age': 30}
]

Or:

sorted_users = sorted(
    users,
    key=lambda user: user["age"]
)

This pattern is worth remembering.

8. Real-World Use Case

Suppose you're processing API data.

If you don't want to modify the original data:

sorted_users = sorted(users, key=lambda x: x["age"])

Use sorted().

If you don't need the original order anymore:

users.sort(key=lambda x: x["age"])

Use sort().

9. Interview-Ready Answer

If the interviewer asks:

What's the difference between sort() and sorted()?

Say:

"sort() is a list method that sorts the list in place and returns None. sorted() is a built-in function that accepts any iterable and returns a new sorted list without modifying the original iterable. I use sort() when I want to modify the existing list and sorted() when I need to preserve the original data."

That's a strong answer.

Quick Memory
list.sort()
→ list only
→ modifies original
→ returns None


sorted(iterable)
→ works with any iterable
→ returns new list
→ original unchanged

"""