"""

1. What is a Serializer in Django REST Framework?

    A Serializer converts complex Python/Django objects into data types that can be rendered as JSON and sent through an API.
    It also does the reverse: it can take incoming JSON data, validate it, and convert it into Python data
    that can be used to create or update objects.

    Think:

        Django Model
            ↓
        Serializer
            ↓
        JSON Response

    And incoming data:

        JSON Request
            ↓
        Serializer
            ↓
        Validated Python Data
            ↓
        Django Model

        
    Example:
        from rest_framework import serializers

        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField()
            age = serializers.IntegerField()

    Then:
        serializer = StudentSerializer(data={
            "name": "Gokul",
            "age": 25
        })

        serializer.is_valid()

    Now:
        serializer.validated_data

    gives:
        {
            "name": "Gokul",
            "age": 25
        }
    
    Interview answer:
        "A serializer in Django REST Framework converts complex objects such as Django model instances into primitive data types that can be rendered as JSON.
        It also validates and deserializes incoming request data into Python data that can be used to create or update objects."

2. What is ModelSerializer?

    ModelSerializer is a specialized serializer that is automatically generated from a Django model.

    Suppose we have:
        class Student(models.Model):
            name = models.CharField(max_length=100)
            age = models.IntegerField()

    Instead of manually defining every serializer field:
        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField()
            age = serializers.IntegerField()

    we can use:
        class StudentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = "__all__"
    
    Django REST Framework automatically generates serializer fields based on the model.


    Interview answer:
        "ModelSerializer is a specialized DRF serializer that automatically generates serializer fields based on a Django model.
        It reduces boilerplate and also provides default implementations for creating and updating model instances."

3. Serializer vs ModelSerializer

| Serializer                                    | ModelSerializer                |
| --------------------------------------------- | ------------------------------ |
| Fields defined manually                       | Fields generated from model    |
| More control                                  | Less boilerplate               |
| Doesn't require a model                       | Designed around a model        |
| Need to implement create/update when required | Provides default create/update |
| Useful for custom/non-model data              | Useful for CRUD APIs           |

Interview answer:
    "Serializer is a base class that allows you to define fields manually and is useful for custom or non-model data.
    ModelSerializer is a subclass of Serializer that automatically generates fields based on a Django model,
    reducing boilerplate code and providing default implementations for creating and updating model instances."


4. Django Shell Command

To open the Django shell:
    python manage.py shell

Then you can interact with your Django models directly.

For example:
    from students.models import Student

        Get all students:
            Student.objects.all()

        Create a student:
            Student.objects.create(name="Gokul")

        Filter:
            Student.objects.filter(name="Gokul")

        Get one:
            Student.objects.get(id=1)

        Exit:
            exit()

Interview answer
    "python manage.py shell opens an interactive Python shell with the Django environment loaded.
    It's useful for testing ORM queries, creating or modifying records, debugging, and experimenting with models."


5. prefetch_related() Example:

Now suppose you want to get all students and their subjects.

Without prefetch_related()

You might write:

students = Student.objects.all()


for student in students:
    print(student.name)


    for subject in student.subjects.all():
        print(subject.name)

Potentially:

1 query → get all students


Then for each student:
1 query → Gokul's subjects
1 query → Priya's subjects
1 query → Thivya's subjects

For 3 students:

1 + 3 = 4 queries

For 100 students:

1 + 100 = 101 queries

That's the N+1 query problem.

7. Using prefetch_related()

Instead:

students = Student.objects.prefetch_related("subjects")

Then:

for student in students:
    print(student.name)


    for subject in student.subjects.all():
        print(subject.name)

Django can fetch the students and related subjects efficiently using separate queries and combine them in Python.

Conceptually:

Query 1:
SELECT * FROM student;


Query 2:
SELECT ...
FROM subject
...

Instead of querying subjects separately for every student.

8. Expected Output

Given:

Gokul  → Tamil, English
Priya  → English, Science
Thivya → Tamil, Science

This:
students = Student.objects.prefetch_related("subjects")

for student in students:
    print(student.name)

    for subject in student.subjects.all():
        print(" -", subject.name)

could output:

Gokul
 - Tamil
 - English

Priya
 - English
 - Science

Thivya
 - Tamil
 - Science

9. Why prefetch_related() Here?

Because we're dealing with:
    ManyToManyField, This is the key point.

select_related()

Generally for:
    ForeignKey
    OneToOneField

    Uses SQL joins.

prefetch_related()

    Generally for:
        ManyToManyField
        Reverse ForeignKey

Uses separate queries and combines the results in Python.

10. Interview-Ready Answer

    If they give you your exact Student/Subject example and ask:

    "Show me a prefetch query."

    Say:
        students = Student.objects.prefetch_related("subjects")


    for student in students:
        print(student.name)

        for subject in student.subjects.all():
            print(subject.name)

    Then explain:
        "Here subjects is a ManyToMany relationship, so I use prefetch_related().
        Without prefetching, accessing student.subjects.all() inside the loop can result in an N+1 query problem. 
        prefetch_related() fetches the related subjects efficiently and associates them with the students in Python."


"""