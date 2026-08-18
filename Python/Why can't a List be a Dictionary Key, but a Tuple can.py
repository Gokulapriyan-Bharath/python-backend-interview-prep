"""
8. Why can't a List be a Dictionary Key, but a Tuple can?

This is a very common follow-up because it tests mutability + hashing + dictionaries together.

1. Basic Theory

A Python dictionary requires its keys to be hashable.

A hashable object must have a hash value that remains stable during its lifetime.

List

A list is mutable:

my_list = [1, 2, 3]


my_list.append(4)

Its contents can change, so it cannot be safely used as a dictionary key.

Therefore:

data = {
    [1, 2, 3]: "value"
}

gives:

TypeError: unhashable type: 'list'
Tuple

A tuple is immutable:

my_tuple = (1, 2, 3)

So a tuple containing only hashable elements can be used as a dictionary key.

data = {
    (1, 2, 3): "value"
}


print(data[(1, 2, 3)])

Output:

value
2. Important Trick: Tuple Is Not Always Hashable

This is where an interviewer can go deeper.

Consider:

data = {
    ([1, 2], 3): "value"
}

This will fail:

TypeError: unhashable type: 'list'

Why?

Although the tuple itself is immutable, it contains a mutable list.

So the tuple cannot be hashed.

Remember:

A tuple is hashable only if all of its elements are hashable.

3. Examples
Valid
key = (1, 2, 3)


print(hash(key))

Works because integers are hashable.

Valid
key = ("Gokul", "Python")


print(hash(key))

Works because strings are hashable.

Invalid
key = ([1, 2], 3)


print(hash(key))

Output:

TypeError: unhashable type: 'list'

Because the tuple contains a list.

4. Why Does the Dictionary Care?

Imagine Python allowed this:

key = [1, 2]


data = {
    key: "hello"
}

Then later:

key.append(3)

The key has changed.

If its hash changed, Python could no longer reliably locate the key in the hash table.

That's why dictionary keys need stable hashing behavior.

5. Real-World Use Case

Tuples are useful as dictionary keys when representing a combination of values.

For example, suppose you want to cache a result based on:

source + destination

You can use:

route_cache = {
    ("Salem", "Chennai"): 320
}

Then:

distance = route_cache[("Salem", "Chennai")]


print(distance)

Output:

320

This pattern is common in caching and memoization.

6. Interview-Ready Answer

If the interviewer asks:

Why can't a list be used as a dictionary key, but a tuple can?

Say:

"Dictionary keys must be hashable. Lists are mutable, so their contents can change and they are therefore unhashable. Tuples are immutable, so a tuple containing only hashable elements can be used as a dictionary key. However, if a tuple contains a mutable object like a list, the tuple itself is also unhashable."

That's an excellent interview answer.

7. Quick Memory Trick
Dictionary key
      ↓
   Hashable?
      ↓
 ┌────┴────┐
Yes        No
 ↓          ↓
Allowed    Error
list       ❌ mutable
dict       ❌ mutable
set        ❌ mutable


str        ✅ immutable
int        ✅ immutable
tuple      ✅ if all elements are hashable
frozenset  ✅ if all elements are hashable

"""