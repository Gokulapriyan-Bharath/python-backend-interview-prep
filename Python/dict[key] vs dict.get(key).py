"""
9. dict[key] vs dict.get(key) in Python

This is simple, but interviewers often use it to check whether you know how Python handles missing dictionary keys.

1. Basic Difference

Suppose we have:

user = {
    "name": "Gokul",
    "role": "Backend Developer"
}
Using dict[key]
print(user["name"])

Output:

Gokul

But if the key doesn't exist:

print(user["age"])

Python raises:

KeyError: 'age'
Using dict.get()
print(user.get("name"))

Output:

Gokul

If the key doesn't exist:

print(user.get("age"))

Output:

None

It doesn't raise KeyError.

2. Providing a Default Value

This is one of the most useful features of .get().

user = {
    "name": "Gokul"
}


age = user.get("age", 0)


print(age)

Output:

0

The syntax is:

dictionary.get(key, default_value)

So:

user.get("age", 0)

means:

"Give me the value of age. If it doesn't exist, give me 0."

3. Practical Backend Example

Imagine you're processing an API request:

data = {
    "name": "Gokul",
    "email": "gokul@example.com"
}

You could do:

name = data.get("name")
phone = data.get("phone")

Output:

name  → "Gokul"
phone → None

This is useful when a field is optional.

For example, in API request processing:

phone = request.data.get("phone")

If the client doesn't send phone, you don't immediately get a KeyError.

4. When Should You Use []?

Use:

data["user_id"]

when the key is required and missing data should be treated as an error.

Example:

user_id = data["user_id"]

If user_id isn't present, getting a KeyError might actually be useful because it tells you the input is invalid.

5. When Should You Use .get()?

Use:

data.get("phone")

when the key is optional.

For example:

phone = data.get("phone")


if phone:
    print("Phone provided")
6. Important Difference

Consider:

data = {
    "age": None
}

Now:

print(data.get("age"))

returns:

None

And:

print(data.get("phone"))

also returns:

None

So .get() alone cannot distinguish between:

Key exists with value None

and:

Key doesn't exist

If you need to distinguish them:

if "age" in data:
    print("Key exists")
7. Interview-Ready Answer

If they ask:

What is the difference between dict[key] and dict.get(key)?

Say:

"dict[key] directly accesses the value and raises a KeyError if the key doesn't exist. dict.get(key) returns the value if the key exists, otherwise it returns None by default, or a specified default value. I use bracket notation when the key is required, and .get() when the key is optional."

That's a strong answer.

8. Quick Comparison
Operation	Key Exists	Key Missing
data["name"]	Value	KeyError
data.get("name")	Value	None
data.get("name", "Unknown")	Value	"Unknown"
Real-world Django example

You'll frequently see:

user_id = request.data.get("user_id")

because API fields aren't always guaranteed to be present.

But if your business logic requires the field, you'd validate it explicitly rather than silently accepting None.

"""