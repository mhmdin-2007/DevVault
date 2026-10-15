::: {align="center"}
# DevVault

### A Community Platform for Developers

**Technical knowledge · Interview preparation · Developer
collaboration**

[![Live
Website](https://img.shields.io/badge/Live%20Website-devvault.ir-6C63FF?style=for-the-badge&logo=google-chrome&logoColor=white)](https://devvault.ir)

[![Django](https://img.shields.io/badge/Django-Web%20Framework-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Nginx-Web%20Server-009639?style=flat-square&logo=nginx&logoColor=white)](https://nginx.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-CSS%20Framework-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

[Open Live Website](https://devvault.ir) · [Source
Code](https://github.com/mhmdin-2007/DevVault)
:::

------------------------------------------------------------------------

## Overview

**DevVault** is a Django-based platform for sharing programming
knowledge, exploring interview questions, and engaging with technical
content.

Unlike a local-only demo, DevVault has a public deployment at
**[devvault.ir](https://devvault.ir)**. This lets visitors explore the
running application and review the implementation in the source
repository.

> **Live application:** <https://devvault.ir>

## Project Overview

**DevVault** is a web platform built to bring developer knowledge,
technical discussions, and interview preparation into one place. It
gives developers a space to explore technical content, share ideas, and
engage with programming questions.

The project is more than a local demo: it has a public website deployed
at **[devvault.ir](https://devvault.ir)**. The repository documents the
application's codebase and the technologies used to run it.

> **Try the live application:** <https://devvault.ir>

## At a Glance

  ---------------------------------- ----------------------------------
  **Project type**                   Full-stack web application

  **Backend**                        Python · Django

  **Database**                       PostgreSQL

  **Web server / reverse proxy**     Nginx

  **Deployment**                     Docker · Docker Compose

  **Frontend**                       Django Templates · Bootstrap ·
                                     HTML · CSS · JavaScript

  **Status**                         Public website deployed
  ---------------------------------- ----------------------------------

## Core Capabilities

> Keep this list aligned with the features currently implemented in the
> production version.

-   **Accounts and profiles** --- user registration, authentication, and
    profile information.
-   **Technical content** --- create and explore posts, articles, and
    interview questions.
-   **Community interaction** --- likes, comments, replies, bookmarks,
    and voting where implemented.
-   **Interview preparation** --- organize technical questions with
    supported categories, difficulty levels, company names, or tags.
-   **Discovery** --- search, filter, and browse content with
    pagination.
-   **Code submissions and attachments** --- support for programming
    answers and file uploads where enabled.

## Technology & Deployment

DevVault uses a conventional Django application stack, with
containerized services to make deployment and service configuration more
repeatable.

  Technology                  Role
  --------------------------- -------------------------------------------------
  **Python**                  Primary programming language
  **Django**                  Server-side web framework and application logic
  **PostgreSQL**              Relational database
  **Nginx**                   Production web server / reverse proxy
  **Docker**                  Containerization
  **Docker Compose**          Multi-service orchestration
  **Bootstrap**               Responsive UI components
  **HTML, CSS, JavaScript**   Frontend structure and behavior
  **Font Awesome**            Icons
  **Git & GitHub**            Version control and source hosting
  **Linux server**            Production hosting environment

The exact versions and any additional services should be verified
against the repository's dependency files and deployment configuration
before release.

## Architecture at a Glance

``` text
                         Visitors
                            |
                            v
                     Public Website
                      devvault.ir
                            |
                            v
                    Nginx / Reverse Proxy
                            |
                            v
                    Django Application
                            |
                            v
                       PostgreSQL
```

This is a high-level view of the production stack. Adapt it if the
actual Nginx, application, or database topology differs from this
diagram.

## Repository Structure

``` text
DevVault/
├── accounts/                  # Account and profile features
├── config/                    # Django project and settings
├── interactions/              # Community interaction features
├── posts/                     # Posts and technical content
├── static/                    # Static source assets
├── templates/                 # Django templates
├── docker/
│   └── nginx/                 # Nginx configuration, if present
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── manage.py
└── requirements.txt
```

Directory names can change between branches. Confirm this tree against
the current repository before publishing.

## Run Locally

### Requirements

-   Git
-   Docker Engine
-   Docker Compose

### 1. Clone the repository

``` bash
git clone https://github.com/mhmdin-2007/DevVault.git
cd DevVault
```

### 2. Configure the environment

If the repository includes an example environment file, copy it:

``` bash
cp .env.example .env
```

Otherwise, create the required environment file based on the variables
referenced by the Compose and Django settings files. Do not commit
secrets or production credentials.

### 3. Build and start the services

``` bash
docker compose up -d --build
```

### 4. Run migrations

Replace `<django-service>` with the service name defined in
`docker-compose.yml`:

``` bash
docker compose exec <django-service> python manage.py migrate
```

### 5. Create an admin user

``` bash
docker compose exec <django-service> python manage.py createsuperuser
```

### 6. Open the local site

Use the host and port configured in Compose. A common local address is:

``` text
http://localhost:8000
```

If the Compose file maps a different port, use the configured address
instead.

## Production Deployment

The repository has a separate production Compose configuration. The
production deployment command used for this project is:

``` bash
docker compose --env-file .env.production -f docker-compose.prod.yml up -d --build
```

Before deploying, verify environment values and confirm that the
production configuration includes the expected settings for:

-   `DEBUG=False` and a secure Django secret key
-   `ALLOWED_HOSTS` and CSRF trusted origins
-   PostgreSQL credentials and persistent storage
-   Nginx routing and static-file delivery
-   HTTPS and production security settings

Run production commands only on the intended server and after reviewing
the configuration.

## Google Search & Public Availability

DevVault has a public website at **[devvault.ir](https://devvault.ir)**.
If the site is appearing in Google Search, that can be highlighted as an
additional milestone---but search visibility and ranking should only be
claimed after checking the actual results or Google Search Console.

To check public indexing, search Google for:

``` text
site:devvault.ir
```

For an authoritative status of indexing, use Google Search Console's URL
Inspection tool. A public website being online does not, by itself,
guarantee that Google has indexed it.

## Configuration & Security

-   Keep credentials and secret keys out of version control.
-   Use a unique production `SECRET_KEY`.
-   Disable Django debug mode in production.
-   Restrict allowed hosts and database access.
-   Use HTTPS for the public site.
-   Back up persistent database data before risky maintenance or
    migrations.

## Testing

Run the checks that are configured for the current codebase. A standard
Django test command is:

``` bash
python manage.py test
```

If running inside Docker, execute it through the actual Django Compose
service. Add specific test, lint, or formatting commands only if they
are configured and maintained in the repository.

## API Documentation

List API routes here only if they are implemented in the current branch.
For each route, document the HTTP method, path, authentication
requirements, request parameters, response format, and a short example.

Do not assume Django REST Framework or specific `/api/` endpoints are
available without confirming them in the codebase.

## Contributing

Contributions and constructive feedback are welcome.

1.  Create a focused branch for your change.
2.  Follow the existing code style.
3.  Run relevant checks.
4.  Explain the change and any configuration updates in your pull
    request.

## License

Confirm the license against the `LICENSE` file in the repository. If the
project uses the BSD 3-Clause License, link that file here.

## Author

**Mohammad Inanloo**

-   **GitHub:** [@mhmdin-2007](https://github.com/mhmdin-2007)
-   **LinkedIn:** [Mohammad
    Inanloo](https://www.linkedin.com/in/mohammad-inanloo-697a0a41/)
-   **Email:** <mhmdin2007@gmail.com>

------------------------------------------------------------------------

::: {align="center"}
**Explore DevVault**

[devvault.ir](https://devvault.ir) · [Source code on
GitHub](https://github.com/mhmdin-2007/DevVault)
:::
