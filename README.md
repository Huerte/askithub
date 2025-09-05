# 🚀 AskItHub

![Homepage](docs/screenshots/Screenshot%20(235).png)

---

<div align="center">

![AskItHub Logo](https://img.shields.io/badge/AskItHub-Community%20Q%26A-25d366?style=for-the-badge&logo=github&logoColor=white)

**A modern community-driven Q&A platform for developers and tech enthusiasts**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2.4-green?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.7-purple?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)

[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## 📖 Table of Contents

- [About The Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
  - [Running the Application](#running-the-application)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [Contributors](#-contributors)
- [License](#-license)
- [Support](#-support)

---

## 🎯 About The Project

**AskItHub** is a modern, community-driven Q&A platform designed specifically for developers and tech enthusiasts. Built with Django and featuring a sleek, responsive UI, it provides an intuitive environment for asking questions, sharing knowledge, and building connections within the tech community.

### 🌟 Why AskItHub?

- **Modern UI/UX**: Beautiful, responsive design with dark theme and glassmorphism effects
- **Community Focused**: Connect with like-minded developers and share knowledge
- **Real-time Features**: Live activity tracking and user engagement
- **Secure Authentication**: Robust user management with password reset functionality
- **Topic Organization**: Categorized questions for better content discovery
- **User Profiles**: Rich user profiles with following/follower system

---

## ✨ Features

### 🔐 Authentication & User Management
- **User Registration & Login**: Secure authentication system
- **Password Reset**: Email-based password recovery with verification codes
- **User Profiles**: Customizable profiles with avatars and bio
- **Follow System**: Follow other users and track their activities

### 💬 Q&A Platform
- **Ask Questions**: Create detailed questions with topics and descriptions
- **Answer System**: Provide helpful answers to community questions
- **Topic Categories**: Organize content by technology topics
- **Search & Discovery**: Find relevant questions and answers easily

### 👥 Community Features
- **User Activity Tracking**: Monitor community engagement
- **Following/Followers**: Build connections with other developers
- **Question Analytics**: View question views and engagement metrics
- **Real-time Updates**: Live activity feed and notifications

### 🎨 Modern UI/UX
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Dark Theme**: Easy on the eyes with professional aesthetics
- **Glassmorphism Effects**: Modern visual design with backdrop blur
- **Interactive Elements**: Smooth animations and hover effects
- **Bootstrap 5**: Latest Bootstrap framework for consistent styling

### 🔧 Admin Features
- **Django Admin**: Full-featured admin interface with Jazzmin theme
- **User Management**: Comprehensive user and content moderation tools
- **Analytics Dashboard**: Monitor platform usage and user engagement

---

## 🛠 Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **Django 5.2.4**: High-level Python web framework
- **SQLite**: Lightweight database for development
- **Django Jazzmin**: Modern admin interface theme

### Frontend
- **Bootstrap 5.3.7**: CSS framework for responsive design
- **Bootstrap Icons**: Icon library for consistent UI
- **HTML5/CSS3**: Modern web standards
- **JavaScript**: Interactive client-side functionality

### Development Tools
- **python-decouple**: Environment variable management
- **Pillow**: Image processing for user avatars
- **Git**: Version control system

---

## 📸 Screenshots

<div align="begin">

### 🏠 Homepage
![Homepage](docs/screenshots/Screenshot%20(235).png)

### 🔐 Authentication Pages
![Login](docs/screenshots/Screenshot%20(236).png)
![Register](docs/screenshots/Screenshot%20(237).png)

### 💬 Q&A Interface
![Questions](docs/screenshots/Screenshot%20(241).png)

### 👤 Profile Page
![Profile](docs/screenshots/Screenshot%20(239).png)
</div>

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Huerte/askithub.git
   cd askithub
   ```

2. **Create a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Environment Setup

1. **Navigate to the Django project directory**
   ```bash
   cd src
   ```

2. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

4. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

### Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Open your browser and navigate to**
   ```
   http://127.0.0.1:8000/
   ```

3. **Access the admin panel at**
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## 📁 Project Structure

```
askithub/
├── .env                         # Environment variables
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── project_enhancement_guide.md # Project enhancement documentation
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
│
├── docs/                        # Documentation and screenshots
│   └── screenshots/             # Application screenshots
│       ├── Screenshot (235).png # Homepage screenshot
│       ├── Screenshot (236).png # Login page screenshot
│       ├── Screenshot (237).png # Register page screenshot
│       ├── Screenshot (239).png # Profile page screenshot
│       └── Screenshot (241).png # Q&A interface screenshot
│
└── src/                         # Django project root
    ├── manage.py                # Django management script
    │
    ├── accounts/                # User authentication & profiles
    │   ├── admin.py             # Admin interface configuration
    │   ├── apps.py              # App configuration
    │   ├── models.py            # User, Profile, UserActivity models
    │   ├── tests.py             # Test cases
    │   ├── urls.py              # Account-related URLs
    │   ├── views.py             # Authentication views
    │   ├── __init__.py          # Python package marker
    │   │
    │   ├── templates/auth/      # Authentication templates
    │   │   ├── login.html       # Login page template
    │   │   ├── register.html    # Registration page template
    │   │   ├── password_reset_request.html    # Password reset request
    │   │   ├── password_reset_verify.html     # Password reset verification
    │   │   └── password_reset_form.html       # Password reset form
    │   │
    │   └── templatetags/        # Custom template tags
    │       ├── subscription_tags.py
    │       └── __init__.py
    │
    ├── core/                    # Core functionality
    │   ├── admin.py             # Admin interface configuration
    │   ├── apps.py              # App configuration
    │   ├── models.py            # Core models
    │   ├── tests.py             # Test cases
    │   ├── urls.py              # Core URLs
    │   ├── views.py             # Core views
    │   └── __init__.py          # Python package marker
    │
    ├── forum/                   # Q&A functionality
    │   ├── admin.py             # Admin interface configuration
    │   ├── apps.py              # App configuration
    │   ├── models.py            # Topic, QuestionThread, Answer models
    │   ├── tests.py             # Test cases
    │   ├── urls.py              # Forum URLs
    │   ├── views.py             # Forum views
    │   ├── __init__.py          # Python package marker
    │   │
    │   └── templates/section/   # Forum templates
    │       └── room.html        # Forum room template
    │
    ├── main/                    # Django settings
    │   ├── asgi.py              # ASGI configuration
    │   ├── settings.py          # Django configuration
    │   ├── urls.py              # Main URL configuration
    │   ├── wsgi.py              # WSGI configuration
    │   └── __init__.py          # Python package marker
    │
    ├── media/                   # User-uploaded files
    │   └── profile_pics/        # User profile pictures
    │
    ├── static/                  # Static files
    │   └── favicon.ico          # Site favicon
    │
    └── templates/               # Base templates
        ├── 400.html             # Bad Request error page
        ├── 401.html             # Unauthorized error page
        ├── 403.html             # Forbidden error page
        ├── 404.html             # Not Found error page
        ├── 500.html             # Server Error error page
        ├── base.html            # Base template
        ├── home.html            # Homepage template
        │
        ├── components/          # Reusable components
        │   ├── footer.html      # Footer component
        │   └── navbar.html      # Navigation component
        │
        └── section/             # Page sections
            ├── about-page.html          # About page
            ├── explore-page.html        # Explore page
            ├── explore-topics-page.html # Explore topics page
            ├── followers-section.html   # Followers section
            ├── following-section.html   # Following section
            ├── profile-page.html        # Profile page
            ├── search-page.html         # Search page
            ├── topics-page.html         # Topics page
            ├── user_activity.html       # User activity page
            │
            ├── contact-section/         # Contact pages
            │   └── contact.html         # Contact page
            │
            └── legal-section/           # Legal pages
                ├── guidelines.html      # Community guidelines
                ├── privacy.html         # Privacy policy
                └── terms.html           # Terms of service
```

---

## 📚 API Documentation

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

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

### Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to keep our community approachable and respectable.

---

## 👥 Contributors

<div align="center">

### 🏆 Project Creators & Maintainers

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Huerte">
        <img src="https://github.com/Huerte.png" width="100px;" alt="Huerte"/>
        <br />
        <sub><b>!HuerteDev</b></sub>
      </a>
      <br />
      <sub>🚀 Full Stack Developer</sub>
    </td>
  </tr>
</table>

---

### 🤝 Want to Contribute?

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

[![Contributors](https://img.shields.io/github/contributors/Huerte/askithub?style=for-the-badge&color=blue)](https://github.com/Huerte/askithub/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/Huerte/askithub?style=for-the-badge&color=green)](https://github.com/Huerte/askithub/network/members)
[![Stars](https://img.shields.io/github/stars/Huerte/askithub?style=for-the-badge&color=yellow)](https://github.com/Huerte/askithub/stargazers)
[![Issues](https://img.shields.io/github/issues/Huerte/askithub?style=for-the-badge&color=red)](https://github.com/Huerte/askithub/issues)

</div>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License** - A short and simple permissive license with conditions only requiring preservation of copyright and license notices.

---

## 🆘 Support

If you need help or have questions about AskItHub:

- **📧 Email**: huertejerald@gmail.com
- **🐛 Bug Reports**: [GitHub Issues](https://github.com/Huerte/askithub/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Huerte/askithub/discussions)
- **📖 Documentation**: [Project Wiki](https://github.com/Huerte/askithub/wiki)

---

<div align="center">

**Made by the AskItHub Community**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Huerte/askithub)

</div>
