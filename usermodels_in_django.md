---

# 🔄 Three Types of User Models in Django

| Class              | Inherit From                          | Customizable?      | Includes fields?                 | When to Use                                                         |
| ------------------ | ------------------------------------- | ------------------ | -------------------------------- | ------------------------------------------------------------------- |
| `User`             | Django's default                      | ❌ Not customizable | ✅ All built-in fields            | When you don’t need to add any extra fields                         |
| `AbstractUser`     | `AbstractBaseUser` + PermissionsMixin | ✅ Yes (add fields) | ✅ All built-in fields            | When you just need to add **extra fields**                          |
| `AbstractBaseUser` | Lowest-level                          | ✅ Fully Custom     | ❌ Only `password` + `last_login` | When you want **complete control** (email login, no username, etc.) |

---

## ✅ 1. `User` (Default Django User Model)

### 🔹 What it gives:

```python
from django.contrib.auth.models import User
```

* Comes with all built-in fields (`username`, `email`, `password`, `first_name`, `last_name`, etc.)
* Comes with all user management features (login, permissions)

### ❌ Cannot be customized

You **can’t add fields** like `user_type` or `phone_number` unless you switch to custom user model.

### ✅ When to Use:

* You’re building a small project
* You don’t need custom roles or extra fields
* You're okay with username + password login

---

## ✅ 2. `AbstractUser` (Extending Default User)

### 🔹 What it gives:

```python
from django.contrib.auth.models import AbstractUser
```

* Everything that the default `User` model gives
* **PLUS** you can **add your own fields**

### ✅ You can add:

```python
class CustomUser(AbstractUser):
    user_type = models.CharField(...)
    phone = models.CharField(...)
```

### ✅ When to Use:

* You want to keep Django’s default fields (username, email, etc.)
* But you also want to add **custom fields**
* Example: You’re building a school system with `student`, `teacher`, and `admin` roles

**✅ This is what you are doing now — and it's the best choice for most apps.**

---

## ✅ 3. `AbstractBaseUser` (Fully Custom Model)

### 🔹 What it gives:

```python
from django.contrib.auth.models import AbstractBaseUser
```

* Gives you **only two things**:

  * `password`
  * `last_login`

You need to:

* Define your own fields like `email`, `username`, etc.
* Define your own manager (UserManager)
* Configure permissions

### ✅ When to Use:

* You want to **completely control** the user model
* You want login via email instead of username
* You're building something non-standard (like an API-only app, or third-party login)

### 🔧 Example Use Cases:

* Login via mobile number
* Login via email only
* Anonymous usernames
* Using external auth (OAuth, Google Sign-in, etc.)

But this is **harder to maintain** — you have to manage:

* `USERNAME_FIELD`
* `REQUIRED_FIELDS`
* Custom `UserManager`
* Permissions

---

## 🔁 Visual Comparison

| Feature            | `User`      | `AbstractUser` | `AbstractBaseUser`      |
| ------------------ | ----------- | -------------- | ----------------------- |
| Add custom fields  | ❌           | ✅              | ✅                       |
| Built-in fields    | ✅           | ✅              | ❌ (only 2 fields)       |
| Permissions ready  | ✅           | ✅              | ❌ (you define)          |
| Custom login logic | ❌           | ❌              | ✅                       |
| Recommended for    | Simple apps | Most apps      | Advanced, flexible apps |

---

## 🧠 Which Should YOU Use?

| Situation                                         | Use                                 |
| ------------------------------------------------- | ----------------------------------- |
| Just need Django's default login, no extra fields | `User`                              |
| Need to add `user_type`, `phone`, etc.            | `AbstractUser` ✅ Best for most apps |
| Want to use email/mobile as login, no username    | `AbstractBaseUser` (advanced)       |

---
