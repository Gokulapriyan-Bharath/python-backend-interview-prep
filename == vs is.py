"""
== vs is in Python

This is another very common interview question.

1. Theory

== and is are completely different.

== — Value comparison

Checks whether two objects have the same value.

is — Identity comparison

Checks whether two variables refer to the exact same object in memory.

Easy way to remember

== → Are the values equal?
is → Are they the same object?

"""

# simple example

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)



# same object example

a = [1, 2, 3]
b = a

print(a == b)
print(a is b)