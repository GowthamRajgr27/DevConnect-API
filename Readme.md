# 🧑‍💻 DevConnect API

A simple social network API built with Django REST Framework where developers can register, create profiles, post projects, and connect with other devs.

## 🚀 Tech Stack
- Python 3
- Django 4
- Django REST Framework
- SQLite (default, can switch to PostgreSQL)
- JWT Authentication (djangorestframework-simplejwt)

## 📦 Features
- Developer registration & login
- Create & manage dev profiles
- Post project showcases
- Follow/unfollow other developers
- Filter developers by skills

## 🔐 Authentication
Uses JWT tokens via `djangorestframework-simplejwt`.

```bash
POST /api/register/
POST /api/login/
Authorization: Bearer <token>


## How to run
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
