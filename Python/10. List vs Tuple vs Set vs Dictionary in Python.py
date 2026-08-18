# List vs Tuple vs Set vs Dictionary in Python

""" 
 This is a fundamental Python interview question.
 The interviewer may ask you to compare them based on ordering, duplicates, mutability, indexing, and use cases.
"""


# 1. Quick Comparison

# | Feature    | List       | Tuple            | Set           | Dictionary     |
# | ---------- | ---------- | ---------------- | ------------- | -------------- |
# | Syntax     | `[]`       | `()`             | `{1, 2}`      | `{"a": 1}`     |
# | Ordered    | ✅          | ✅             | ❌*           | ✅**          |
# | Mutable    | ✅          | ❌             | ✅            | ✅            |
# | Duplicates | ✅          | ✅             | ❌            | Keys: ❌      |
# | Indexing   | ✅          | ✅             | ❌            | By key        |
# | Key-value  | ❌          | ❌             | ❌            | ✅            |
# | Hashable   | ❌          | ✅***          | ❌            | Keys must be   |
# | Main use   | Collection | Fixed collection | Unique values  | Key-value data |


"""
* Sets don't support positional indexing and shouldn't be treated as ordered sequences.
** Dictionaries preserve insertion order in modern Python.
*** A tuple is hashable only if all of its elements are hashable.

2. List

A list is:

Ordered + Mutable + Allows duplicates

skills = ["Python", "Django", "Python"]


print(skills)
print(skills[0])

Output:

['Python', 'Django', 'Python']
Python

You can modify it:

skills.append("FastAPI")
Use case

Use a list when:

Order matters
You need to modify the collection
Duplicates are allowed

Example:

users = ["Gokul", "Rahul", "Arun"]
3. Tuple

A tuple is:

Ordered + Immutable + Allows duplicates

coordinates = (11.66, 78.14)


print(coordinates[0])

Output:

11.66

You can't do:

coordinates[0] = 12.0

This raises:

TypeError
Use case

Use a tuple when the collection represents fixed data.

Examples:

coordinates = (11.66, 78.14)


rgb = (255, 255, 255)

Tuples can also be used as dictionary keys if all their elements are hashable.

4. Set

A set is:

Mutable + Unique elements + No positional indexing

skills = {"Python", "Django", "Python"}


print(skills)

Output will contain:

{'Python', 'Django'}

The duplicate "Python" is removed.

You can add:

skills.add("FastAPI")
Use case

Use a set when you care about uniqueness.

For example:

skills = ["Python", "Django", "Python", "FastAPI"]


unique_skills = set(skills)


print(unique_skills)
5. Dictionary

A dictionary stores:

Key → Value

user = {
    "name": "Gokul",
    "role": "Backend Developer",
    "experience": 3
}

Access:

print(user["name"])

Output:

Gokul

Keys must be unique:

user = {
    "name": "Gokul",
    "name": "Rahul"
}


print(user)

Output:

{'name': 'Rahul'}

The second value replaces the first.

Use case

Dictionaries are ideal for:

JSON-like data
API responses
Configuration
Fast key-based lookup
6. Real Backend Example

Imagine an API returns:

user = {
    "id": 101,
    "name": "Gokul",
    "skills": ["Python", "Django"],
    "roles": {"developer", "admin"},
    "location": (11.66, 78.14)
}

Here:

dict     → user data
list     → skills that can change
set      → unique roles
tuple    → fixed coordinates

This is a nice way to understand when each data structure makes sense.

7. Time Complexity

This can be a follow-up interview question.

| Operation    |           List | Tuple |      Set |             Dict |
| ------------ | -------------: | ----: | -------: | ---------------: |
| Index access |           O(1) |  O(1) |        ❌ | By key: O(1) avg |
| Search       |           O(n) |  O(n) | O(1) avg |         O(1) avg |
| Append/Add   | O(1) amortized |     ❌ | O(1) avg |         O(1) avg |
| Delete       |           O(n) |     ❌ | O(1) avg |         O(1) avg |



🧠 Easy Memory Trick


LIST
→ Ordered
→ Mutable
→ Duplicates

TUPLE
→ Ordered
→ Immutable
→ Duplicates

SET
→ Unique
→ No indexing
→ Fast membership

DICT
→ Key → Value
→ Unique keys
→ Fast lookup

"""