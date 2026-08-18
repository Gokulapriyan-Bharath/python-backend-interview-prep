"""
7. How does a Python Dictionary work internally?

This is a good one because it connects directly to the hashing question you just studied.

1. Theory

A Python dictionary is a hash table-based data structure that stores data as:

key → value

For example:

user = {
    "name": "Gokul",
    "age": 25
}

When you do:

user["name"]

Python doesn't simply scan every key one by one.

It uses the hash of the key to efficiently locate the corresponding entry.

Conceptually:

"name"
   ↓
hash("name")
   ↓
hash table
   ↓
find entry
   ↓
"Gokul"

That's why dictionary lookup is O(1) average time complexity.

2. Practical Example
users = {
    "gokul": "Backend Developer",
    "rahul": "Frontend Developer",
    "arun": "DevOps Engineer"
}


print(users["gokul"])

Output:

Backend Developer

Python hashes "gokul" and uses that information to locate the value.

3. What Happens Internally?

Conceptually, when you do:

users["gokul"]

Python does something similar to:

1. Calculate hash of "gokul"
              ↓
2. Use hash to identify a table location
              ↓
3. Check the key stored there
              ↓
4. If necessary, handle a collision
              ↓
5. Return the associated value

You don't need to explain CPython's exact internal implementation unless the interviewer specifically asks.

4. What is a Hash Collision?

Two different keys can sometimes produce the same hash value.

For example, conceptually:

hash("key1") → 12345
hash("key2") → 12345

This is called a hash collision.

Python has mechanisms for handling collisions rather than simply assuming every hash is unique.

So remember:

Hash values don't have to be unique.

The dictionary still checks the actual key for equality when necessary.

5. Why Must Dictionary Keys Be Hashable?

Consider:

data = {
    "name": "Gokul"
}

"name" is hashable.

But:

data = {
    [1, 2, 3]: "numbers"
}

fails:

TypeError: unhashable type: 'list'

A dictionary needs keys whose hash/equality behavior is stable while they're being used as keys.

That's why immutable types such as:

str
int
tuple (if its contents are hashable)
frozenset

can be dictionary keys.

6. Time Complexity

This is another thing interviewers may ask.

Operation	Average
Lookup	O(1)
Insert	O(1)
Delete	O(1)
Search by value	O(n)

For example:

users["gokul"]

is average O(1).

But:

"Backend Developer" in users.values()

requires potentially checking many values, so it's O(n).

7. Real-World Use Case

Dictionaries are everywhere in backend development.

For example, an API response:

response = {
    "user_id": 101,
    "name": "Gokul",
    "role": "Backend Developer",
    "active": True
}

Or caching:

cache = {}


cache["user:101"] = user_data

Then:

user_data = cache.get("user:101")

The average O(1) lookup makes dictionaries very useful for these use cases.

8. Interview-Ready Answer

If they ask:

How does a Python dictionary work internally?

You can say:

"A Python dictionary is a hash-table-based data structure that stores key-value pairs. Python calculates the hash of the key and uses it to efficiently locate the corresponding entry. Dictionary lookup, insertion, and deletion are O(1) on average. If a hash collision occurs, Python has mechanisms to resolve it and also compares the actual keys when necessary. Dictionary keys must be hashable, which is why mutable types like lists cannot be used as keys."

That's a strong interview-level answer.

"""