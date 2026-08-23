<div align="center">

# AskItHub

<p align="center">
  <img src="docs/screenshots/Screenshot%20(235).png" alt="AskItHub Banner" width="100%" />
</p>

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](#)
[![Platform](https://img.shields.io/badge/platform-Web-blueviolet.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Huerte/askithub.svg)](#)

**A modern community-driven Q&A platform for developers and tech enthusiasts.**

[Report a Bug](https://github.com/Huerte/askithub/issues) · [Request a Feature](https://github.com/Huerte/askithub/issues)

</div>

---

<p align="center">
  Built with Django and featuring a sleek, responsive UI, AskItHub provides an intuitive environment for asking questions, sharing knowledge, and building connections within the tech community.
</p>

---

## Table of Contents

- [Installation Guide](#installation-guide)
- [What It Does](#what-it-does)
- [Demo](#demo)
- [How It Works](#how-it-works)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)
- [Support](#support)

---

## Installation Guide

Follow these steps to install AskItHub locally.

### Prerequisites

| What you need | Where to get it |
|---------------|-----------------|
| Python 3.8+   | [python.org](https://www.python.org/downloads/) |
| Git           | Already on your machine |
| pip           | Included with Python |

### Build from Source

**Steps:**

1. Clone the repository:
   ```bash
   git clone https://github.com/Huerte/askithub.git
   cd askithub
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Database & Migration:
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Run the Server:
   ```bash
   python manage.py collectstatic
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/`. (Admin at `/admin/`)

---

## What It Does

| Feature | What it means |
|---------|---------------|
| **Q&A Platform** | Ask detailed questions, provide answers, organize by tech topics, and easily search content. |
| **Community Tracking** | Live activity feeds, question analytics, and a robust follower system for building connections. |
| **Secure Authentication** | Full user registration, password recovery, and customizable rich profiles. |
| **Modern UI/UX** | A dark theme with glassmorphism effects, responsive on all devices via Bootstrap 5. |
| **Admin Dashboard** | Full-featured moderation tools and analytics powered by the Django Jazzmin theme. |

---

## Demo

> Visual overview of the AskItHub platform.

### Homepage
<p align="center">
  <br>
  <img alt="Homepage" src="docs/screenshots/Screenshot%20(235).png" width="800" />
  <br>
</p>

### Authentication Pages
<p align="center">
  <br>
  <img alt="Login" src="docs/screenshots/Screenshot%20(236).png" width="800" />
  <br>
</p>
<p align="center">
  <br>
  <img alt="Register" src="docs/screenshots/Screenshot%20(237).png" width="800" />
  <br>
</p>

### Q&A Interface
<p align="center">
  <br>
  <img alt="Questions" src="docs/screenshots/Screenshot%20(241).png" width="800" />
  <br>
</p>

### Profile Page
<p align="center">
  <br>
  <img alt="Profile" src="docs/screenshots/Screenshot%20(239).png" width="800" />
  <br>
</p>

---

## How It Works

**Project structure:**

```text
askithub/
├── .env                         # Environment variables
├── docs/                        # Documentation and screenshots
└── src/                         # Django project root
    ├── accounts/                # User authentication & profiles
    ├── core/                    # Core functionality
    ├── forum/                   # Q&A functionality
    ├── main/                    # Django settings and URL routing
    ├── media/                   # User-uploaded files
    ├── static/                  # Static CSS, JS, and Images
    ├── templates/               # Global HTML base templates
    └── manage.py                # Django management script
```

---

## API Documentation

### Authentication Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/accounts/login/` | POST | User login |
| `/accounts/register/` | POST | User registration |
| `/accounts/forgot-password/` | POST | Password reset request |
| `/accounts/verify-code/` | POST | Password reset verification |
| `/accounts/reset-password/` | POST | Password reset completion |

### Forum Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/forum/` | GET | List all questions |
| `/forum/ask/` | POST | Create new question |
| `/forum/question/<id>/` | GET | View specific question |
| `/forum/answer/<id>/` | POST | Add answer to question |
| `/forum/topics/` | GET | List all topics |

### User Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/profile/<username>/` | GET | View user profile |
| `/profile/<username>/follow/` | POST | Follow/unfollow user |
| `/profile/<username>/activity/` | GET | View user activity |

---

## Contributing

Contributions are welcome. Here is how to go from zero to a submitted pull request.

### Getting Started

**Prerequisites:** Python 3.8+ and Git.

**Fork and clone:**

```
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/askithub.git
cd askithub

# 2. Keep your fork in sync with the original
git remote add upstream https://github.com/Huerte/askithub.git
```

### Making Changes

**Branch naming:**

```
feat/short-description    # New features
fix/short-description     # Bug fixes
docs/short-description    # Documentation only
chore/short-description   # Maintenance or refactoring
```

**Commit messages:** Use plain English. Describe what changed and why:

```
# Good
git commit -m "feat: add user activity tracking dashboard"
git commit -m "fix: resolve password reset email delivery issue"
git commit -m "docs: clarify database setup in README"

# Avoid
git commit -m "fix stuff"
git commit -m "update"
```

**Code style:**

- Follow PEP 8 Python style guidelines.
- Follow the existing Django conventions in the project.
- Add tests for new features.
- Never swallow exceptions silently.

### Submitting a Pull Request

1. Push your branch to your fork:
   ```
   git push origin feat/your-feature
   ```

2. Open a Pull Request against `Huerte/askithub:main` on GitHub.

3. In the PR description, briefly explain: what you changed, why, and how to test it.

4. If your change affects the app's output or behavior, update this README accordingly.

---

## Contributors

<div align="center">
  <table>
    <tr>
      <td align="center"><a href="https://github.com/Huerte"><img src="https://github.com/Huerte.png" width="80px;" alt=""/></a><br /><a href="https://github.com/Huerte"><b>!HuerteDev</b></a></td>
    </tr>
  </table>
</div>

---

## License

Distributed under the **MIT** License. See [`LICENSE`](LICENSE) for details.

---

## Support

If you need help or have questions about AskItHub:

- **Email**: huertejerald@gmail.com
- **Bug Reports**: [GitHub Issues](https://github.com/Huerte/askithub/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Huerte/askithub/discussions)

---

*Built to provide an intuitive environment for asking questions and sharing knowledge.*
