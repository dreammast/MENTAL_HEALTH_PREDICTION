# Campus Mind - Mental Health Chatbot

A comprehensive mental health support platform for college students featuring AI-powered chatbot, mood tracking, mindfulness exercises, and career guidance.

## Features

- 🤖 **AI Chatbot**: Powered by LangChain and Groq LLM
- 📝 **Mood Tracker**: Track daily moods with notes and history
- 🧠 **Mindfulness Exercises**: Guided breathing, meditation, and relaxation
- 👥 **Peer Support**: Connect with other students
- 🩺 **Therapist Sessions**: Book appointments with licensed professionals
- 📚 **Self-Help Resources**: Articles, videos, and workbooks
- 🎯 **Career Assessment**: Personalized career guidance and skill development

## Deployment Options

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:
   ```bash
   heroku create campus-mind-chatbot
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Deploy**:
   ```bash
   git init
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

5. **Open your app**:
   ```bash
   heroku open
   ```

### Option 2: Railway

1. **Connect to Railway**:
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Set environment variables in Railway dashboard

2. **Set environment variables**:
   - `GROQ_API_KEY`: Your Groq API key

3. **Deploy**: Railway will automatically deploy from your repository

### Option 3: Render

1. **Connect to Render**:
   - Go to [render.com](https://render.com)
   - Create a new Web Service
   - Connect your GitHub repository

2. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - Set environment variables

### Option 4: VPS/Cloud Server

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   export GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run with Gunicorn**:
   ```bash
   gunicorn app:app --bind 0.0.0.0:8000
   ```

4. **Use Nginx** as reverse proxy (optional)

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)
- `FLASK_ENV`: Set to 'production' for production deployment

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   export GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open** http://localhost:5000

## API Endpoints

- `GET /`: Main application interface
- `POST /api/chat`: Chat with the AI bot

## File Structure

```# 🎓 CampusX Event Portal

[![Java](https://img.shields.io/badge/Java-17+-ED8B00?logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.3-6DB33F?logo=springboot&logoColor=white)](https://spring.io/projects/spring-boot)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Maven](https://img.shields.io/badge/Maven-3.8+-C71A36?logo=apachemaven&logoColor=white)](https://maven.apache.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**CampusX Event Portal** is a full-stack campus event management system. Students can browse events, register, manage wishlists, earn downloadable certificates, and pay for events; admins can manage events and approve payments — all with a modern dark-themed UI and JWT-secured REST API.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| **Events** | Browse by category (Technical, Cultural, Hackathon, Sports, Academic, Workshop), filter by date/status, view details and register |
| **Registrations** | One-click registration, cancel anytime; optional paid events with UPI/bank payment and admin approval |
| **Wishlist** | Save events for later; add/remove from dashboard or event cards |
| **Certificates** | View and download PDF certificates for attended events (generated on-the-fly with iText 7) |
| **Dashboard** | Stats, upcoming events, activity feed, quick access to registrations, certificates, wishlist, profile, notifications |
| **Admin** | Create events, view stats, approve payment screenshots |
| **Auth** | JWT-based login/register; BCrypt password hashing; protected API routes |

---

## 🛠 Tech Stack

- **Backend:** Java 17, Spring Boot 3.3, Spring Security, JPA/Hibernate, JJWT, iText 7 (PDF)
- **Database:** MySQL 8
- **Frontend:** Vanilla HTML5, CSS3, JavaScript (no frameworks)
- **Build:** Maven

---

## 📋 Prerequisites

| Tool | Version |
|------|---------|
| [Java](https://adoptium.net/) | 17+ |
| [Maven](https://maven.apache.org/download.cgi) | 3.8+ |
| [MySQL](https://dev.mysql.com/downloads/) | 8.0+ |

---

## 🚀 Quick Start

### 1. Clone and enter the project

```bash
git clone https://github.com/YOUR_USERNAME/campus-event-portal.git
cd campus-event-portal
```

### 2. Create and seed the database

```bash
# Create database and tables
mysql -u root -p < src/main/resources/db/schema.sql

# Seed 12 mock events + demo data (registrations, wishlist, certificates, notifications)
Get-Content src/main/resources/db/seed_events.sql | mysql -u root -p campusx
```

On Linux/macOS:

```bash
mysql -u root -p campusx < src/main/resources/db/seed_events.sql
```

### 3. Configure database (optional)

Edit `src/main/resources/application.properties` if your MySQL user/password differ:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/campusx?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true
spring.datasource.username=root
spring.datasource.password=YOUR_PASSWORD
```

### 4. Run the application

```bash
mvn spring-boot:run
```

Then open **http://localhost:8080** in your browser.

---

## 📁 Project Structure

```
campus-event-portal/
├── pom.xml
├── README.md
├── src/main/
│   ├── java/com/campusx/
│   │   ├── CampusXApplication.java
│   │   ├── config/          # JWT, Security
│   │   ├── controller/      # REST API
│   │   ├── dto/
│   │   ├── entity/          # JPA entities
│   │   └── repository/
│   └── resources/
│       ├── application.properties
│       ├── db/
│       │   ├── schema.sql
│       │   └── seed_events.sql
│       └── static/          # Frontend (HTML, CSS, JS)
│           ├── index.html
│           ├── events.html
│           ├── dashboard.html
│           ├── login.html, register.html
│           ├── certificate-preview.html
│           ├── admin-login.html, admin-dashboard.html
│           ├── css/style.css
│           └── js/main.js, js/admin.js
```

---

## 🌐 API Overview

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register` | No | Register |
| POST | `/api/auth/login` | No | Login (returns JWT) |
| GET | `/api/events` | No | List events (category, status, month, search) |
| GET | `/api/events/{id}` | No | Get event by ID |
| GET | `/api/registrations` | JWT | My registrations |
| POST | `/api/registrations` | JWT | Register for event |
| PATCH | `/api/registrations/{id}/cancel` | JWT | Cancel registration |
| GET | `/api/certificates` | JWT | My certificates |
| GET | `/api/certificates/{id}/download` | JWT | Download certificate PDF |
| GET | `/api/wishlist` | JWT | My wishlist |
| POST | `/api/wishlist` | JWT | Add to wishlist |
| DELETE | `/api/wishlist/{eventId}` | JWT | Remove from wishlist |
| GET | `/api/dashboard/stats` | JWT | Dashboard stats |
| GET | `/api/dashboard/activity` | JWT | Activity feed |
| GET | `/api/notifications` | JWT | Notifications |

---

## 🔐 Demo Access

- **Student:** Register at http://localhost:8080/register.html or use existing seeded users (see `seed_events.sql`).
- **Admin:** http://localhost:8080/admin-login.html (admin credentials in `admin.js`; change in production).

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend HTML template
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version
└── README.md            # This file
```

## Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- Consider implementing rate limiting for production
- Add authentication if needed for your use case

## Support

For issues or questions, please check the documentation or create an issue in the repository.

