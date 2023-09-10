## Directory Structure

```
flask-web-app-boilerplate/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
│   │   └── images/
│   │       ├── logo.png
│   │       └── user_default.jpg
│   │
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── profile/
│   │   │   ├── view_profile.html
│   │   │   └── edit_profile.html
│   │   ├── errors/
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── base.html
│   │   └── index.html
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── search_history.py
│   │   └── email_notifications.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   └── profile_routes.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── email_service.py
│   │   └── search_service.py
│   │
│   ├── config.py
│   └── run.py
│
├── tests/
│   ├── test_models.py
│   ├── test_views.py
│   └── test_utils.py
│
├── .gitignore
├── requirements.txt
└── README.md
```
