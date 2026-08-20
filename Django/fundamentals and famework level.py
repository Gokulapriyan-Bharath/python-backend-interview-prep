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

    
9. Django Project vs Django App
    Django Project
        A project is the overall Django application/configuration.

    For example:

        myproject/
            manage.py
            myproject/
                settings.py
                urls.py
                wsgi.py
                asgi.py

    Django App
        An app is a specific component that handles a particular business/domain functionality.

    For example:

        students/
            models.py
            views.py
            serializers.py
            urls.py
            admin.py

        You might have:

        myproject
        ├── users
        ├── students
        ├── payments
        └── subscriptions
    
    Interview answer
        "A Django project represents the overall application and its configuration,
        while a Django app is a modular component that implements a specific functionality or business domain.
        A single Django project can contain multiple apps."

    Easy way to remember

    Project = entire application

    App = one feature/domain inside it

    
10. Django Request-Response Lifecycle

    Suppose the client sends:

    GET /students/

    The flow is roughly:

    Client
    ↓
    Web Server
    ↓
    WSGI / ASGI
    ↓
    Middleware
    ↓
    URL Resolver
    ↓
    View
    ↓
    ORM / Database
    ↓
    View
    ↓
    Middleware
    ↓
    Response
    ↓
    Client
    Step-by-step
    Step 1 — Request arrives

    The client sends an HTTP request.

    GET /students/
    Step 2 — WSGI/ASGI receives it

    Depending on your deployment/application type, Django receives the request through its WSGI or ASGI interface.

    Step 3 — Middleware

    Django processes the request through the configured middleware stack.

    Examples:

    Authentication
    Sessions
    CSRF
    Security
    Custom middleware
    Step 4 — URL Resolver

    Django checks:

    urlpatterns = [
        path("students/", views.student_list),
    ]

    and determines which view should handle the request.

    Step 5 — View

    The view executes:

    def student_list(request):
        students = Student.objects.all()
        ...
    Step 6 — Database

    The ORM may query the database.

    Step 7 — Response

    The view returns:

    return JsonResponse(data)

    Step 8 — Middleware again

    The response passes back through the middleware stack.

    Step 9 — Client receives response

    The client receives the HTTP response.

    Interview answer
    "A request enters Django through WSGI or ASGI, passes through the middleware stack,
    and is resolved by the URL dispatcher to the appropriate view. The view can interact with models and the database, 
    then creates a response. The response passes back through middleware before being returned to the client


11. What is manage.py
    manage.py is a command-line utility for interacting with a Django project.

    Examples:
        python manage.py runserver
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
        python manage.py shell

    Interview answer
        "manage.py is a Django project-specific command-line utility. 
        It sets up the Django environment for that project and allows us to run management commands such as migrations,
        starting the development server, creating a superuser, and opening the Django shell."

12. What is the difference between a QuerySet and a Manager?
    QuerySet:   
        A QuerySet represents a collection of database queries and results. It is lazy and can be filtered, sliced, and evaluated.

    Manager:
        A Manager is a Django class that provides an interface for database query operations on a model. 
        It is the entry point for creating QuerySets.
    
13. What is settings.py?

    settings.py is a configuration file for a Django project. It contains settings for database connections, 
    installed apps, middleware, templates, static files, security options, and other project-level configurations.

    Interview answer:
        "settings.py contains the configuration of a Django project, including installed apps, middleware,
        database configuration, templates, static files, security settings, and other project-level settings."


14. What is the difference between a Model and a Form in Django?
    Model:
        A Model is a Python class that defines the structure of a database table and its fields. 
        It represents the data layer of the application.

    Form:
        A Form is a Python class that defines how to handle user input, validation, and rendering of HTML forms. 
        It represents the presentation layer for user input.

    Interview answer:
        "A Model defines the structure of the database and represents data, while a Form handles user input,
        validation, and rendering of HTML forms. Models are used for data storage, while Forms are used for user interaction."

15. What is urls.py?
    urls.py is a configuration file that defines URL patterns and maps them to views in a Django project. 
    It acts as the URL dispatcher, determining which view should handle a given request based on the requested URL.

    Interview answer:
        "urls.py contains URL patterns that map incoming requests to the appropriate views. 
        It allows us to define the routing of our application and organize our views based on URLs."

    Example:

    from django.urls import path
    from . import views

    urlpatterns = [
        path("students/", views.student_list),
    ]

    When a request comes to:
        /students/

    Django maps it to:
        views.student_list



16. What is wsgi.py?
    wsgi.py is a configuration file that serves as the entry point for WSGI-compatible web servers to serve a Django project. 
    It exposes the WSGI callable that the server uses to communicate with the Django application.

    Interview answer:
        "wsgi.py contains the WSGI application callable that allows WSGI-compatible web servers to serve the Django project. 
        It sets up the Django environment and provides an interface for handling HTTP requests."

17. What is asgi.py?
    asgi.py is a configuration file that serves as the entry point for ASGI-compatible web  
    servers to serve a Django project.
    It exposes the ASGI callable that the server uses to communicate with the Django application.           

    Interview answer:
        "asgi.py contains the ASGI application callable that allows ASGI-compatible web servers to serve the Django project.
        It sets up the Django environment and provides an interface for handling asynchronous 
        HTTP requests and WebSocket connections." 


18. What is Middleware?
    Middleware is a framework of hooks into Django's request/response processing. 
    It is a lightweight, low-level plugin system for globally altering Django's input or output.

    Middleware components are executed in order for each request and response. 
    They can perform functions such as authentication, session management, CSRF protection, and more.

    Common Django middleware:
        MIDDLEWARE = [
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
        ]
    
    Middleware can be used for:
        Authentication
        Logging
        Security
        Request tracking
        Custom logic that should apply across multiple views


    Interview answer:
        "Middleware is a layer that processes requests before they reach the view and responses before they are returned to the client. 
        It's useful for cross-cutting concerns such as authentication, logging, security, request tracking, 
        and other logic that should apply across multiple views."


































































































































































































































































































































































































































































































































































































































































































































































































"""