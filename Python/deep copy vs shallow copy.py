# Shallow Copy vs Deep Copy

"""
Shallow Copy

A shallow copy creates a new outer object, but the objects inside it are still shared references.

So:

Outer object → copied
Nested objects → shared

Deep Copy

A deep copy creates a completely independent copy, including the nested objects.

So:

Outer object → copied
Nested objects → also copied"""


import copy

original = {
    "name": "Gokul",
    "skills": ["Python", "Django"]
}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

"""
now We've

original
   |
   ├── name → "Gokul"
   |
   └── skills ──→ ["Python", "Django"]

shallow
   |
   ├── name → "Gokul"
   |
   └── skills ──→ SAME list

deep
   |
   ├── name → "Gokul"
   |
   └── skills ──→ NEW list
    
    That's the entire concept.

"""


# Shallow Copy Example

original = {
    "name": "Gokul",
    "skills": ["Python", "Django"]
}

shallow = copy.copy(original)

shallow["skills"].append("FastAPI")

print(original)
print(shallow)


# Deep Copy Example


original = {
    "name": "Gokul",
    "skills": ["Python", "Django"]
}

deep = copy.deepcopy(original)

deep["skills"].append("FastAPI")

print(original)
print(deep)


# The Interview-Trick Example


a = {
    "user": {
        "name": "Gokul"
    }
}

b = a.copy()

b["user"]["name"] = "Rahul"

print(a)
print(b)

"""
This surprises people.

Why?

Because .copy() on a dictionary performs a shallow copy.

The outer dictionaries are different:

a != b  # different dictionary objects

But the nested "user" dictionary is shared:

a["user"] is b["user"]
→ True
"""



# Deep copy version

a = {
    "user": {
        "name": "Gokul"
    }
}

b = copy.deepcopy(a)

b["user"]["name"] = "Rahul"

print(a)
print(b)

# Now they're completely independent.


"""
When Would You Use Each?

    Use shallow copy when:
        You only need a new outer container.
        Nested objects are intentionally shared.
        The data isn't deeply nested.
        You want to avoid the extra cost of deep copying.


    Use deep copy when:
        You need a completely independent object.
        The structure contains nested mutable objects.
        Changes to nested data must not affect the original.

"""


"""
Quick Comparison                        Shallow Copy 	    Deep Copy
Outer object	                            New	                New
Nested objects	                            Shared	            New
Independent nested modifications?	        ❌ No	          ✅ Yes
Memory usage	                            Lower	            Higher
Performance	                                Faster	            Slower
Python	                                    copy.copy()	        copy.deepcopy()

"""