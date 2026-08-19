"""

1. Theory

ORM stands for Object-Relational Mapping.

Django ORM allows you to interact with the database using Python objects and QuerySets instead of writing SQL directly.

For example, suppose we have:

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

Instead of writing SQL:

SELECT * FROM student;

you can use Django ORM:

students = Student.objects.all()

Django converts the ORM operation into the appropriate SQL query.


2. Practical Examples

Get all students
    Student.objects.all()

Get one student
    Student.objects.get(id=1)

Filter students
    Student.objects.filter(age=20)

Create a student
    Student.objects.create(
        name="Gokul",
        age=25
    )

Update
    Student.objects.filter(id=1).update(age=26)

Delete
    Student.objects.filter(id=1).delete()



3. Why Do We Use ORM?

The main benefits are:

Less raw SQL
Pythonic database access
Model-based abstraction
Query composition through QuerySets
Database portability
Easier integration with Django models

But don't say "ORM eliminates SQL."

Django ORM still generates SQL underneath.


Follow-UP questions

1. What is a QuerySet?
    A QuerySet is a collection of database queries represented by Django ORM.
    It allows us to retrieve, filter, and manipulate objects from the database.
    QuerySets are lazy, so the database query is generally executed only when the QuerySet is evaluated.


Example:
    students = Student.objects.filter(age=20)


2. What does lazy evaluation mean in Django?
    "Lazy evaluation means Django doesn't immediately execute the database query when we create or modify a QuerySet. 
    The query is executed when we actually need the results, 
    such as when iterating over the QuerySet or converting it to a list."

Example:

    students = Student.objects.filter(age=20)

    # Query is evaluated here
    for student in students:
        print(student.name)
    
        
3. What is the difference between filter() and get()?

    This is very important.

    filter()
        Returns a QuerySet, potentially containing multiple objects.

        students = Student.objects.filter(age=20)

    It can return:
        0 objects
        1 object
        10 objects
    
    get()

        Returns exactly one object.
    
        student = Student.objects.get(id=1)

        If no object exists:
            DoesNotExist

        If multiple objects match:
            MultipleObjectsReturned
    
    Interview answer:
        "filter() returns a QuerySet and can return zero or multiple objects. get() expects exactly one object; 
        it raises DoesNotExist if no object matches and MultipleObjectsReturned if multiple objects match."

        
4. Does filter() immediately hit the database?

    "Generally, no. filter() returns a lazy QuerySet. The database query is executed when that QuerySet is evaluated."

    students = Student.objects.filter(age=20)

    Then:

    list(students)

    evaluates it.

5. What is the difference between first() and get()?

    first():
        student = Student.objects.filter(age=20).first()
        Returns:
            First matching object
            None if nothing matches
    
    get():
        student = Student.objects.get(id=1)
        Requires exactly one matching object.

    Interview answer:
        "first() returns the first matching object or None,
        while get() expects exactly one object and raises exceptions when zero or multiple objects match."

        
6. What is the difference between exists() and count()?
    exists() checks whether at least one row exists:
        
        Student.objects.filter(age=20).exists() Returns True or False.

    count() counts the matching rows:
    
        Student.objects.filter(age=20).count() Returns an integer.

    Interview answer:
        If I only need to know whether a record exists,
        I use exists() rather than count(), because I don't need the total number of records

7. What is values()?
    values() returns dictionaries instead of model instances.

    students = Student.objects.values("id", "name")

    Example result:
        [
            {"id": 1, "name": "Gokul"},
            {"id": 2, "name": "Arun"}
        ]
    
    Interview answer:
        values() is useful when I only need specific fields rather than complete model instances. It returns dictionaries.

        
8. What is values_list()?

    It returns tuples instead of dictionaries.

    Student.objects.values_list("id", "name")

    Result:
        [
            (1, "Gokul"),
            (2, "Arun")
        ]

    You can also use:
        Student.objects.values_list("name", flat=True)
    
    Result:
        ["Gokul", "Arun"]

        
9. What is the N+1 query problem?

    Suppose you have:
        students = Student.objects.all()

        for student in students:
            print(student.subject.name)
    
    You might execute:
        1 query → get students
        N queries → get subject for each student

    So if you have 100 students:
        1 + 100 = 101 queries
    
    That's the N+1 query problem.

    Interview answer:
        The N+1 problem occurs when we execute one query to retrieve a collection and then execute an additional query for each object's related data.
        This can cause a large number of database queries. 
        In Django, we commonly solve this using select_related() or prefetch_related()
            

10. select_related() vs prefetch_related()?

This is one of the most important Django questions.*

select_related()
    Used mainly for:
        ForeignKey
        OneToOneField
    
    It uses SQL JOIN.
        students = Student.objects.select_related("subjects")

        
    Conceptually:
        SELECT ...
        FROM student
        JOIN subject ...

prefetch_related()
    Used mainly for:
        ManyToManyField
        Reverse ForeignKey
    
    It uses two separate queries and does the joining in Python.
        students = Student.objects.prefetch_related("subjects")

    Conceptually:
        SELECT ... FROM student
        SELECT ... FROM subject WHERE student_id IN (...)       

    Interview answer:
        select_related() is generally used for single-valued relationships like ForeignKey and OneToOne and uses SQL joins. 
        prefetch_related() is used for multi-valued relationships like ManyToMany and reverse ForeignKey 
        and performs separate queries that Django combines in Python.

        
11. What is only()?
    only() allows you to load only specific model fields initially.

    Student.objects.only("id", "name")

    Useful when the model has many fields but you only need a few.

    Be careful: accessing deferred fields later can trigger additional queries

    
12. What is defer()?
    The opposite idea:

    Student.objects.defer("large_description")

    It tells Django not to load that field initially.

    Again, accessing the deferred field later may trigger another query.  

13. What is order_by()?

    Used to sort QuerySet results.

    Student.objects.order_by("name")

    Descending:
        Student.objects.order_by("-name")

        The - means descending order.    

14. What is exclude()?

    It returns objects that don't match a condition.
    
    Student.objects.exclude(age=20)

    Conceptually:
        WHERE age != 20

15. Can QuerySets be chained?

    Yes.

    students = (
        Student.objects
        .filter(age__gte=18)
        .exclude(name="Gokul")
        .order_by("name")
    )

    Django builds the query from these operations.
    
    Interview answer:
    "Yes. Django QuerySets are chainable,
    which allows us to build complex queries incrementally while keeping the code readable."

"""