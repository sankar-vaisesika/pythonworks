## 🌱 **Week 1: Django Basics & Setup**

> *Goal: Understand Django's structure, setup, and basic components.*

### 📅 Day 1-2: Django Introduction + Installation

* What is Django? Features of Django.
* Install Python & Django (via `pip`).
* Create a virtual environment.
* Create your first Django project (`django-admin startproject`).
* Run development server (`python manage.py runserver`).

💡 **Exercise:** Create a “Hello, World” Django app.

---

### 📅 Day 3-4: Django Project Structure

* Understand project files: `settings.py`, `urls.py`, `wsgi.py`, `manage.py`
* Difference between *project* and *app*.
* Create a new app (`python manage.py startapp`).

💡 **Exercise:** Create an app called `blog` and connect it to your project.

---

### 📅 Day 5-7: URLs + Views + Templates

* Define URLs (`urls.py`) at project & app level.
* Write basic views (function-based views).
* Render templates (HTML with Django template syntax).

💡 **Exercise:**
✅ Create 3 pages: Home, About, Contact — each with different URLs/views/templates.

---

## 🏗 **Week 2: Models, Admin, Forms**

> *Goal: Understand database integration & Django ORM.*

### 📅 Day 8-9: Models & Migrations

* Define models (fields, `__str__`)
* Run migrations (`makemigrations`, `migrate`)
* QuerySet basics (`Model.objects.all()`)

💡 **Exercise:** Create a `Post` model with `title`, `content`, `created_at`.

---

### 📅 Day 10-11: Django Admin

* Register models in `admin.py`
* Customize admin list display

💡 **Exercise:** Add several posts through the admin panel and display them on your site.

---

### 📅 Day 12-14: Forms & GET/POST

* Understand forms (`forms.py`)
* Handle form submissions
* CSRF token

💡 **Exercise:** Create a simple comment form for posts.

---

## ⚡ **Week 3: Advanced Features**

> *Goal: Build a dynamic app with CRUD operations.*

### 📅 Day 15-16: CRUD Operations

* Create, update, delete views (function-based)
* Use Django generic views

💡 **Exercise:** Implement full CRUD for your `Post` model.

---

### 📅 Day 17-18: Static & Media Files

* Add CSS, JS to templates.
* Configure static/media files.

💡 **Exercise:** Style your blog with basic CSS.

---

### 📅 Day 19-20: User Authentication

* User model basics
* Login, logout, signup
* Decorators like `@login_required`

💡 **Exercise:** Restrict post creation to logged-in users.

---

### 📅 Day 21: Messages Framework

* Use messages to display feedback (success, error)

💡 **Exercise:** Show success message after login or post creation.

---

## 🚀 **Week 4: Project + Deployment Prep**

> *Goal: Build your mini-project and prepare for deployment.*

### 📅 Day 22-24: Build Your Mini Project

👉 Example: Blog / Notes app / To-do app

* Combine what you’ve learned
* Design models, views, templates
* Add authentication

---

### 📅 Day 25-26: Pagination + Filters

* Add pagination to post list
* Filter posts by logged-in user or category

💡 **Exercise:** Paginate post list (5 per page)

---

### 📅 Day 27: Custom Error Pages

* Create custom 404, 500 templates

---

### 📅 Day 28-29: Deployment

* Explore deployment options: PythonAnywhere, Heroku
* Collect static files
* Understand environment variables

---

### 📅 Day 30: Review + Next Steps

* Review key concepts: models, views, templates, forms
* Plan enhancements (e.g., add REST API, DRF)

---


