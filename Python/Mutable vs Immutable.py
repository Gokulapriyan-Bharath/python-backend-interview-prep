# Mutable and Immutable

"""
 Mutable objects are objects whose state can be modified after creation.
 Examples are list, dictionary, and set. Immutable objects cannot be modified after creation. Examples are integers, strings, tuples, and booleans. When we appear to modify an immutable object, Python creates a new object instead of changing the existing one.
"""

numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

# The existing list was modified.

# So, list is mutable.

# Practical Example — String

name = "Gokul"

name = name + "apriyan"

print(name)

"""
It might look like the original string was modified, but that's not what happened.

Python created a new string object.

Strings are immutable.

"""

name = "Gokul"

print(id(name))

name = name + " Kumar"

print(id(name))

# The object ID will generally be different because a new string object was created.


# 1. Is a tuple always immutable?

# The tuple itself is immutable, but it can contain mutable objects.

data = ([1, 2], 3)

data[0].append(4)

print(data)

# The tuple structure didn't change, but the list inside it changed.

# This is a very good advanced interview point.


# 3. Does immutable mean memory can never change?

# No. Be careful here.

# Immutable means the object's state cannot be changed.

# Python can still create a new object and make a variable reference it.

# x = 10
# x = 20

# The variable x changed what it refers to; the integer object 10 wasn't modified.