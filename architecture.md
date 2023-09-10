# Flask Web App Boilerplate System Architecture

```
+---------------------+
|                     |
|    Web Browser      |
|                     |
+----------+----------+
           |
           |
+----------V----------+
|                     |
|      Flask App      |
|                     |
+----------+----------+
           |
           |
+----------V----------+
|                     |
|    Database (DB)    |
|                     |
+---------------------+
```

### Components:

- **Web Browser**: The user interface where users interact with the application.
- **Flask App**: The backend server handling HTTP requests and responses, routing requests to appropriate view functions, and serving dynamic content using Jinja2.
- **Database (DB)**: The storage system where application data is persisted. SQLAlchemy provides an abstraction layer to interact with the database using Python code.
