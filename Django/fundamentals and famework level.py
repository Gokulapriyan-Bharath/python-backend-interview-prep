"""
        Django fundamentals and framework-level interview

1. What is Django?
    "Django is a high-level, open-source Python web framework used for building web applications and APIs. 
    It follows the Model-Template-View architecture and
    provides built-in features like ORM, authentication, middleware, URL routing, admin interface, security mechanisms,
    and database support."

2. Why Django?

Interview-ready answer:
    I would choose Django when I need to build a robust backend quickly because it provides many features out of the box,
    such as ORM, authentication, admin interface, URL routing, middleware, security features, and database integration.
    It also has a mature ecosystem and follows a structured architecture, which makes it suitable for building 
    and maintaining large applications."

Simple version:
    Django gives you many backend features out of the box, so you don't have to build everything from scratch.

    
3. What are the advantages of Django?
    
    1. Batteries Included    
        Django provides many built-in features:
            ORM
            Authentication
            Admin panel
            URL routing
            Middleware
            Forms
            Security features
            Sessions
            Caching support

            This is often called the "batteries-included" philosophy.

    2. Rapid Development:
        Django allows developers to build applications quickly due to its built-in features and structured architecture.

        For example:
            class Student(models.Model):
                name = models.CharField(max_length=100)
        
        Django handles a lot of the database interaction through the ORM.


    3. Security
        Django provides protections and secure defaults for common web vulnerabilities, including:
            CSRF
            SQL injection through parameterized ORM queries
            Clickjacking
            XSS-related protections
            Secure password handling

    But don't say:
        "Django makes the application completely secure."
        It doesn't. Developers still need to implement security correctly.


    4. Scalability

        Django can support large applications when properly designed.

        Scaling isn't simply a property of the framework. You also need things like:

        Database optimization
        Caching
        Load balancing
        Background jobs
        Horizontal scaling
        Efficient queries

    This distinction is good to mention in interviews.


    5. Mature Ecosystem
        Django has been around for a long time and has a large ecosystem.
        You also have Django REST Framework for building REST APIs.

    6. Admin Interface
        One of Django's biggest productivity advantages is the built-in admin interface.

        Once you define models, you can register them:
            from django.contrib import admin

            admin.site.register(Student)

    Django can then provide an admin interface for managing those records.


4. Why Django Instead of Flask?

Don't say:
    "Django is better than Flask."

That's too simplistic.

Instead:
    It depends on the project requirements. Django is a batteries-included framework,
      so I would prefer it when I need a structured application with built-in ORM, authentication, admin, 
      middleware, and other common features. Flask is more lightweight and minimal, 
      so I might choose it when I want more control over the architecture or 
      I'm building a smaller service with fewer framework-level requirements.
    

      
5. Why Django for a Microservice? This is a slightly tricky question.

Don't automatically say:
    "Django is best for microservices."

Instead:
    For a microservice, I would choose the framework based on the service's requirements.
    Django can be used when the service needs features such as ORM, authentication, admin,
    or a more structured application architecture.
    For a lightweight service with simple APIs, I might consider Flask or FastAPI because they have less framework overhead.
      

6. Why Django REST Framework?
    Django REST Framework, or DRF, provides tools for building RESTful APIs on top of Django.
    It provides serializers, authentication, permissions, viewsets, routers, pagination, filtering, throttling,
    and API validation, which makes API development much easier.


7. What is Django's Architecture?
    Django is commonly described as following MTV — Model, Template, View.
        Request
        ↓
        URL Routing
        ↓
        View
        ↓
        Model / ORM
        ↓
        Database
        ↓
        View
        ↓
        Template
        ↓
        Response
    
    For an API application, the template layer may not be involved; the view can return JSON through DRF.

    Interview answer:
        Django follows an MTV architecture. Models represent data and database interaction, 
        Views contain request-handling logic, and Templates handle presentation. 
        Django's URL dispatcher maps incoming requests to the appropriate view.

8. What is Django's biggest advantage?
    Its biggest advantage is productivity: Django provides a mature, 
    batteries-included ecosystem with ORM, authentication, admin, routing, middleware, security features, and 
    other components out of the box, while still providing a structured architecture for larger applications.



    



"""