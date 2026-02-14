# 🎬 WATCHMATE(IMDB Clone) API – Django REST Framework Project

A fully functional backend API built using **Django** and **Django REST Framework** for managing movies, streaming platforms, user accounts, and reviews. This project implements secure authentication, JWT token support, permissions, throttling, and full CRUD functionality.

---

# 🚀 Features

* User Registration, Login, and Logout
* JWT and Token based Authentication
* Admin Dashboard
* Streaming Platform Management
* WatchList (Movies/Shows) Management
* Review System
* User-specific Reviews
* Permissions & Security
* Throttling to prevent abuse
* Fully RESTful API design

---

# 🛠️ Tech Stack

* Backend: Django
* API Framework: Django REST Framework
* Authentication: JWT (SimpleJWT) and Token based
* Database: SQLite (default) / PostgreSQL (recommended for production)
* Language: Python

---

# 📂 API Endpoints

Base URL:

```
http://127.0.0.1:8000/
```

---

# 1️⃣ Admin Access

Access the Django admin dashboard:

```
http://127.0.0.1:8000/admin/
```

Admin can:

* Manage users
* Manage streaming platforms
* Manage watchlist items
* Manage reviews

---

# 2️⃣ Accounts

### Register User

```
POST /watch/account/register/
```

### Login User

```
POST /watch/account/login/
```

Returns:

* User specific token in case of token based authentication.
* access token and refresh token in case of jwt authentication.


---

### Logout User

```
POST /watch/account/logout/
```

Invalidates user session/token.

---

# 3️⃣ Stream Platforms

### Create Platform / List Platforms

```
GET, POST /watch/stream/
```

---

### Retrieve, Update, Delete Specific Platform

```
GET, PUT, DELETE /watch/stream/<int:streamplatform_id>/
```

Example:

```
/watch/stream/1/
```

---

# 4️⃣ Watch List (Movies / Shows)

### Create Movie / List Movies

```
GET, POST /watch/
```

---

### Retrieve, Update, Delete Specific Movie

```
GET, PUT, DELETE /watch/<int:movie_id>/
```

Example:

```
/watch/5/
```

---

# 5️⃣ Reviews

### Create Review for Specific Movie

```
POST /watch/<int:movie_id>/review-create/
```

---

### List All Reviews for Specific Movie

```
GET /watch/<int:movie_id>/reviews/
```

---

### Retrieve, Update, Delete Specific Review

```
GET, PUT, DELETE /watch/reviews/<int:review_id>/
```

Example:

```
/watch/reviews/3/
```

---

# 6️⃣ User Reviews

### Get All Reviews by Specific User

```
GET /watch/user-reviews/?username=example
```

Returns all reviews written by that user.

---

# 🔐 Authentication

This project uses JWT authentication and token authentication

After login, include the access token in headers:

```
for token based Authorization: Token <your_access_token>
for JWT Authorization: Bearer <your_access_token>
```

Example:

```
Authorization: Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```
git clone <your_repo_url>
cd watchlist-project
```

---

## 2. Create Virtual Environment

```
python -m venv env
```

Activate:

Mac/Linux:

```
source env/bin/activate
```

Windows:

```
env\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Run Migrations

```
python manage.py migrate
```

---

## 5. Create Superuser

```
python manage.py createsuperuser
```

---

## 6. Run Server

```
python manage.py runserver
```

---

# 🧪 Testing

You can test endpoints using:

* Postman
* Curl
* Thunder Client (VS Code)

---

# 🔒 Security Features Implemented

* JWT Authentication and token authentication
* User Permissions
* Authenticated-only endpoints
* Throttling protection
* User-specific access control
* Secure password hashing

---

# 📌 Project Structure

```
watchmate-project/
│
├── user_app/
├── watchlist_app/
├── watchmate/
├── manage.py
└── requirements.txt
```

---

# 📈 Future Improvements

* Deploy to AWS / Render / DigitalOcean
* Add Redis caching
* Add email verification
* Add Docker support
* Connect React frontend
* Add CI/CD pipeline

---

# 👨‍💻 Author

Developed as a full-featured production-ready backend API using Django REST Framework - Kunal Garg

---

# 📜 License

This project is open-source and free to use.
