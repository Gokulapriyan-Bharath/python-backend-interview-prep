# What hashing algorithm is used for strings in Python?

"""

1. Theory

In CPython, Python uses SipHash for hashing strings.

More specifically, modern CPython uses SipHash-1-3 for string hashing by default.

The important reason is security. Python uses randomized hashing to make hash-flooding attacks much harder.

You can see the hash using:

text = "hello"


print(hash(text))

The exact number is not something you should rely on.

2. Important Point: Hash Randomization

If you run:

print(hash("hello"))

in one Python process and then restart Python and run it again, you may get a different value.

Example:

Process 1:
-123456789


Process 2:
987654321

That's because Python uses a randomized hash seed for strings.

You can see the current process's hash seed behavior through:

import os


print(os.environ.get("PYTHONHASHSEED"))

If PYTHONHASHSEED isn't explicitly set, Python normally chooses a random seed at startup.

3. Why Does Python Randomize String Hashes?

Consider a dictionary:

users = {
    "gokul": 100,
    "rahul": 200,
    "arun": 300
}

Dictionaries use hashing to efficiently locate keys.

An attacker could potentially send specially crafted keys that produce many hash collisions. This could cause excessive CPU usage.

Randomized hashing makes it much harder for an attacker to predict collisions across processes.

So the key interview point is:

SipHash + hash randomization → protection against hash-flooding attacks.

4. Why Does a String Need to Be Hashable?

Strings are commonly used as dictionary keys:

user = {
    "name": "Gokul",
    "role": "Backend Developer"
}

Python needs to calculate a hash for "name" and "role" so the dictionary can efficiently locate the corresponding values.

You can verify:

print(hash("name"))
5. Hashable vs Mutable

This connects directly to the mutable vs immutable question we just studied.

A dictionary key needs to be hashable.

For example:

data = {
    "name": "Gokul"
}

Works because strings are hashable.

But:

data = {
    [1, 2, 3]: "numbers"
}

raises:

TypeError: unhashable type: 'list'

Why?

Because lists are mutable.

If a mutable object were allowed as a dictionary key and its contents changed, its hash could become inconsistent with its location in the dictionary.

6. Tuple Example

A tuple can be a dictionary key:

data = {
    (10, 20): "point"
}


print(data[(10, 20)])

Output:

point

But there's an important detail.

This works:

(10, 20)

because the tuple contains hashable integers.

But this doesn't:

([10, 20], 30)

because the tuple contains a mutable list.

hash(([10, 20], 30))

gives:

TypeError: unhashable type: 'list'

"""