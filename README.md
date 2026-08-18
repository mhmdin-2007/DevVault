# DevVault

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-5.1.4-green.svg)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/postgresql-15+-blue.svg)](https://postgresql.org)
[![Docker](https://img.shields.io/badge/docker-27+-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/license-BSD_3--Clause-red.svg)](LICENSE)

> A community-driven platform for software engineers to share interview questions, algorithm challenges, and technical knowledge.

DevVault is a Django-based web platform designed around **technical learning, interview preparation, and developer collaboration**.

The platform allows developers to share technical content, discuss programming problems, interact with other developers, and organize useful resources for future reference.

---

## 📖 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation with Docker](#installation-with-docker)
- [Environment Variables](#environment-variables)
- [Database](#database)
- [API](#api)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

##  Features

### 👤 Authentication & Profiles

* User registration and login with validation
* Developer profiles with avatar, bio, and social links
* Follow / unfollow developers

### 📝 Content Management

* Multiple content types:

  * Social posts
  * Interview questions
  * Articles
* Image and video support
* Company and tag categorization
* SEO-friendly slug-based URLs

### 💬 Community Interaction

* Likes on posts and answers
* Nested comments and replies
* Upvote / downvote system
* Bookmarking
* Answers to interview questions
* Answer acceptance by the question author
* File uploads for programming answers such as `.py` and `.cpp`

### 🔎 Search & Filtering

* Full-text search across titles and content
* Filtering by:

  * Post type
  * Category
  * Difficulty
  * Company
  * Tags
* Pagination for large result sets

### 🐳 Dockerized Development

* Docker-based development environment
* Docker Compose configuration
* PostgreSQL database
* Persistent database volumes
* Simple project setup

---

##  Tech Stack

### Backend

| Technology        | Version | Purpose                   |
| ----------------- | ------: | ------------------------- |
| Python            |   3.11+ | Programming language      |
| Django            |   5.1.4 | Web framework             |
| PostgreSQL        |     15+ | Database                  |
| Django ORM        |       — | Database abstraction      |
| GenericForeignKey |       — | Polymorphic relationships |

### Frontend

| Technology       | Version | Purpose               |
| ---------------- | ------: | --------------------- |
| Bootstrap        |     5.3 | UI framework          |
| Font Awesome     |     6.4 | Icons                 |
| Django Templates |       — | Server-side rendering |

### DevOps & Tools

| Technology     | Purpose                     |
| -------------- | --------------------------- |
| Docker         | Containerization            |
| Docker Compose | Multi-container development |
| Git            | Version control             |

---

## Project Structure

```text
DevVault/
├── accounts/          # Authentication and user profiles
├── config/            # Django project configuration
├── interactions/      # Likes, comments, votes and bookmarks
├── posts/             # Posts, articles and interview content
├── static/            # Static assets
├── staticfiles/       # Collected static files
├── templates/         # Django templates
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Git
* Python 3.11+
* Docker
* Docker Compose

PostgreSQL 15+ is required when running the project without Docker.

---

## Installation with Docker

### 1. Clone the repository

```bash
git clone https://github.com/mhmdin-2007/DevVault.git
cd DevVault
```

### 2. Create the environment file

```bash
cp .env.example .env
```

Configure the required environment variables inside `.env`.

### 3. Build and start the containers

```bash
docker-compose up -d
```

### 4. Run database migrations

```bash
docker exec -it devvault_web bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Open the application

```text
http://localhost:8000
```

Admin panel:

```text
http://localhost:8000/admin
```

---

## Environment Variables

Sensitive configuration should be stored in `.env` and should not be committed to the repository.

Use `.env.example` as a template for local configuration.

---

## Database

DevVault uses **PostgreSQL** as its primary database and Django ORM for database interaction.

The project also uses Django's relational modeling capabilities to manage relationships between users, posts, comments, answers, votes, bookmarks, and other entities.

---

##  API

The project includes **REST API** endpoints built with **Django REST Framework**.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/posts/` | List all posts |
| POST | `/api/posts/` | Create a new post |
| GET | `/api/posts/{id}/` | Retrieve a post |
| PUT | `/api/posts/{id}/` | Update a post |
| DELETE | `/api/posts/{id}/` | Delete a post |
| GET | `/api/users/` | List all users |
| GET | `/api/users/{id}/` | Retrieve a user |

---

##  Future Improvements

Potential future improvements include:

* Automated testing and increased test coverage
* API documentation
* UI/UX With professional Design 
* CI/CD pipeline
* Production deployment
* Performance optimization
* Additional developer-focused features

---

##  License

This project is licensed under the **BSD 3-Clause License**.

---
##  Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature: your-feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

### Code Style
- Follow **PEP 8** for Python code
- Use **Class-Based Views** where possible
- Write **docstrings** for functions and classes
- Keep **templates** clean and organized
##  Author

**Mohammad Inanloo**

* GitHub: [@mhmdin-2007](https://github.com/mhmdin-2007)
* LinkedIn: [Mohammad Inanloo](https://www.linkedin.com/in/mohammad-inanloo-697a0a41/)
* Email: [mhmdin2007@gmail.com](mailto:mhmdin2007@gmail.com)
