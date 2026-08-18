
# These are used when you don't know in advance how many arguments a function will receive.

"""
1. *args

*args allows a function to accept any number of positional arguments.
"""

def add_numbers(*args):
    print(args)

add_numbers(10, 20, 30, 40)

# Notice that args becomes a tuple.

# You can loop through it:

def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add_numbers(10, 20, 30))


# Remember *args → variable number of positional arguments → stored as a tuple.



"""
**kwargs

**kwargs allows a function to accept a variable number of keyword arguments.
"""


def user_info(**kwargs):
    print(kwargs)

user_info(name="Gokul", age=25, role="Developer") # kwargs becomes a dictionary.


def user_info(**kwargs):
    print(kwargs["name"])
    print(kwargs["role"])

user_info(name="Gokul", role="Developer")



# Using Both Together


def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(10, 20, 30, name="Gokul", role="Developer")



"""
Very Important — Unpacking

* and ** are also used for unpacking.

List/Tuple unpacking

"""

numbers = [10, 20, 30]

print(*numbers) # The * unpacks the list into separate positional arguments.



# dictionary unpacking

user = {
    "name": "Gokul",
    "role": "Developer"
}

def display_user(name, role):
    print(name, role)

display_user(**user) # **user unpacks the dictionary into keyword arguments.