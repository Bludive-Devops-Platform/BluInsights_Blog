# BluInsights Tech Blog - Project README

## Project Overview

BluInsights is a comprehensive tech blogging platform built to demonstrate full-stack integration of multiple services. The project showcases best practices in backend and frontend development, API communication, microservices architecture, authentication, and content management. It is designed for BluDive Technologies as a proof-of-concept POC to manage blog posts, comments, and admin functionalities efficiently.

The platform consists of the following components:

* **Frontend**: HTML, CSS, JavaScript SPA that consumes APIs from backend services.
* **User Service**: Handles authentication and admin management.
* **Blog Service**: Manages CRUD operations for blog posts.
* **Comment Service**: Handles user comments on blog posts.

The application demonstrates a real-world tech blogging platform with admin control, dynamic content updates, media uploads, and comment management..

## 🏗 Architecture Overview

The system is composed of **microservices** that communicate via HTTP and JSON. Below is a high-level architecture diagram:

                           ┌─────────────────────┐
                           │     Frontend        │
                           │ (HTML/CSS/JS SPA)   │
                           │                     │
                           │ - Home Feed         │
                           │ - Admin Login       │
                           │ - Create/Edit Posts │
                           │ - View Comments     │
                           └─────────┬───────────┘
                                     │ HTTPS / API Calls
                                     ▼
        ┌──────────────┐      ┌───────────────┐      ┌──────────────────┐
        │ User Service │◀────▶│ Blog Service │◀────▶│ Comment Service │
        │  (Node.js)   │      │  (FastAPI)    │      │    (Go)          │
        │ - JWT Auth   │      │ - CRUD Blogs  │      │ - CRUD Comments  │
        │ - Profile    │      │ - Image URL   │      │ - Timestamp      │
        │ - Admins     │      │ - Author ID   │      │ - User ID        │
        └─────┬────────┘      └─────┬─────────┘      └─────┬────────────┘
              │                     │                      │
              ▼                     ▼                      ▼
        ┌─────────────┐        ┌──────────────┐      ┌─────────────┐
        │   MongoDB   │        │  SQLite DB   │      │ SQLite DB   │
        │(Users/Admins)│       │ (Blogs)      │      │ (Comments)  │
        └─────────────┘        └──────────────┘      └─────────────┘
                                     │
                                     ▼
                             ┌───────────────┐
                             │ Local / NFS   │
                             │ Storage       │
                             │ (Images)      │
                             └───────────────┘


---

## Features

### General Features

* Admin login and registration for content management.
* Create, read, update, delete (CRUD) operations for blog posts.
* Dynamic comments system linked to posts.
* File uploads for blog post header images.
* Search and filter functionality for posts.
* Responsive design compatible with mobile and desktop devices.
* Hero carousel for showcasing featured topics.

### Admin-Specific Features

* Access to create, edit, and delete blog posts.
* Posts are linked to the admin username.
* Admin-only registration and login.

### Blog Features

* Blog posts display title, author, content, tags, creation date, and header image.
* Latest posts appear first in the feed.
* Individual post pages with comment section.

### Comment Features

* Users can post comments on blog posts.
* Comments include username and timestamp.
* Comments dynamically update without page reload.

---

## Project Structure

```
BluInsights/
├── backend/
│   ├── user-service/        # Node.js + Express service for authentication
│   ├── blog-service/        # Python FastAPI service for blog CRUD
│   ├── comment-service/     # Go + Gin service for comments
├── frontend/                # HTML/CSS/JS SPA
└── README.md                # This file
```

### Backend Services

1. **User Service**

   * Node.js + Express
   * JWT-based authentication
   * Endpoints for login, registration, and profile fetch
   * Stores user credentials and admin info

2. **Blog Service**

   * Python FastAPI
   * SQLite database (POC) for blog posts
   * Endpoints for create, read, update, delete posts
   * Supports image uploads for headers
   * Returns JSON for frontend consumption

3. **Comment Service**

   * Go + Gin framework
   * SQLite database for comments
   * Endpoints: GET `/comments/:postId`, POST `/comments/:postId`
   * Stores comment text, username, and timestamp

### Frontend

* SPA built with HTML, CSS, and vanilla JS
* Consumes backend APIs for blogs, users, and comments
* Implements dynamic rendering, login state management, and CRUD operations
* Hero section carousel for featured posts
* Search and filter for posts
* Admin-only controls for creating, editing, deleting posts

---

## Getting Started

### Prerequisites

* Node.js (for User Service)
* Python 3.12+ (for Blog Service)
* Go 1.24+ (for Comment Service)
* SQLite3
* Browser for frontend testing

### Running the Services

#### User Service

```
cd backend/user-service
npm install
npm start
```

#### Blog Service.

```
cd backend/blog-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 5001
```

#### Comment Service

```
cd backend/comment-service
go mod tidy
go run main.go
```

### Running Frontend

Simply open `frontend/index.html` in your browser. Ensure that backend services are running on their respective ports:

* User Service: 5050
* Blog Service: 5001
* Comment Service: 5002

---

## Usage

1. Open the frontend in your browser.
2. Admin can navigate to login/register section.
3. After login, admin can create new posts using the form.
4. Posts are displayed dynamically in the feed, latest first.
5. Users can view post details, add comments, and see existing comments.
6. Admin can edit or delete their own posts.
7. Search box allows filtering posts by title or content.
8. Hero section cycles through featured images automatically.

---

## Tech Stack

* **Frontend**: HTML5, CSS3, JavaScript (ES6+)
* **User Service**: Node.js, Express, JWT, SQLite
* **Blog Service**: Python, FastAPI, SQLAlchemy, SQLite
* **Comment Service**: Go, Gin, GORM, SQLite
* **Media**: Local storage for images (header images for blogs)

---

## Project Highlights

* Multi-service architecture demonstrating microservices interaction.
* Fully functional CRUD for blog management.
* Admin authentication and role-based access control.
* Dynamic and responsive frontend SPA.
* Comment system with real-time updates.
* File upload handling and dynamic media rendering.

---

## Contact

For questions or support regarding this project, contact **BluDive Technologies Ltd.**

---

*BluInsights - Bringing tech insights to life.*


