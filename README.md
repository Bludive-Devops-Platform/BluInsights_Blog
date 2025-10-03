# BluInsights – Full Tech Blog Platform

![BluInsights Logo](images/logo.png)

## Overview

**BluInsights** is a modern, full-stack tech blogging platform developed by BluDive Technologies. It is designed to showcase insights, tutorials, and technical articles in DevOps, Cloud, Cybersecurity, AI/ML, and Productivity. The platform is modular, with separate services for user management, blog posts, comments, and file uploads, ensuring scalability, maintainability, and clean separation of concerns.

BluInsights serves as both a demonstration of modern DevOps workflows and a production-ready internal blogging platform for technical teams.

---

## Architecture

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│ User Service│──────▶│ Blog Service│──────▶│ CommentSvc  │       │ File Service│
│  (Node.js)  │       │ (Python)    │       │ (Go + Gin)  │       │  (Node.js)  │
└─────────────┘       └─────────────┘       └─────────────┘       └─────────────┘
       ▲                     ▲                   ▲
       │                     │                   │
       └──────Frontend───────┘                   │
                (HTML, CSS, JS)                  │
                                                 ▼
                                           Image Storage (local/NFS)
```

* **User Service**: Handles authentication, JWT-based sessions, and admin/user profiles.
* **Blog Service**: Manages blog posts with full CRUD support, including images.
* **Comment Service**: Manages comments per blog post.
* **File Service**: Handles header image uploads and provides URL access.

---

## Features

### Core Features

* Admin-controlled blog creation, editing, and deletion.
* User authentication via JWT (only admin accounts allowed for post management).
* Dynamic frontend displaying latest blog posts at the top.
* Real-time comment system for each blog post.
* Hero section with sliding banner images.
* Tag-based filtering and search functionality.
* Responsive design for desktop and mobile.

### Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend Services**:

  * User Service – Node.js + Express + SQLite/MongoDB
  * Blog Service – Python + FastAPI + SQLite
  * Comment Service – Go + Gin + SQLite
  * File Service – Node.js + Express
* **Authentication**: JWT
* **Storage**: Local filesystem (images), SQLite (data)
* **DevOps Tools**: Docker (optional), Git, VSCode, WSL/Ubuntu

---

## Folder Structure

```
backend/
├── user-service/
├── blog-service/
├── comment-service/
└── file-service/

frontend/
└── index.html
```

Each backend service is self-contained and can run independently.

---

## Service-Specific READMEs

### 1. User Service (Node.js + Express)

**Purpose**: Handles authentication, registration, and admin profile management.

#### Endpoints

* `POST /api/login` – Admin login (returns JWT token)
* `POST /api/register` – Admin registration (optional)
* `GET /api/profile` – Fetch admin profile info

#### Setup

```bash
cd backend/user-service
npm install
npm start
```

#### Notes

* JWT secret and DB URL stored in `.env`.
* Only registered admins can create, edit, and delete blog posts.

---

### 2. Blog Service (Python + FastAPI)

**Purpose**: Handles blog CRUD operations.

#### Endpoints

* `POST /blogs` – Create blog post (admin only)
* `GET /blogs` – List all blog posts
* `GET /blogs/{id}` – Get specific blog post
* `PUT /blogs/{id}` – Update blog post (admin only)
* `DELETE /blogs/{id}` – Delete blog post (admin only)

#### Setup

```bash
cd backend/blog-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 5001
```

#### Notes

* Stores blog title, content, tags, author, and image URL.
* Supports image uploads via File Service.
* Blog posts are displayed in reverse chronological order on the frontend.

---

### 3. Comment Service (Go + Gin)

**Purpose**: Manages comments for blog posts.

#### Endpoints

* `GET /comments/{postId}` – Fetch comments for a blog post
* `POST /comments/{postId}` – Add a comment

#### Setup

```bash
cd backend/comment-service
go mod tidy
go run main.go
```

#### Notes

* Each comment stores `user_id`, `text`, and `created_at` timestamp.
* Comments are displayed in reverse chronological order.

---

### 4. File Service (Node.js + Express)

**Purpose**: Handles header image uploads.

#### Endpoints

* `POST /upload` – Upload image (returns URL for Blog Service)

#### Setup

```bash
cd backend/file-service
npm install
npm start
```

#### Notes

* Images are saved to local filesystem or NFS.
* URL is used by Blog Service to display images in posts.

---

## Frontend Usage

* Open `frontend/index.html` in a browser or serve via HTTP server.
* Hero images can be updated via the `/images` folder.
* Admin login enables full CRUD for posts.
* Search box filters posts by title or content in real-time.
* New posts appear at the top of the feed.

---

## Admin Workflow

1. Admin registers or logs in.
2. Creates, edits, or deletes blog posts.
3. Posts include optional header images.
4. Comments can be viewed and moderated.
5. Hero images displayed via sliding carousel on homepage.

---

## Contribution

1. Clone the repository.
2. Install dependencies per service.
3. Run each service locally.
4. Make changes in your branch.
5. Submit a pull request for review.

---

## Notes

* Only admin users can manage posts. General visitors can view posts and leave comments.
* All services communicate via REST APIs with JSON payloads.
* Images are served via File Service or Blog Service.
* Designed for full DevOps-friendly deployment and modular extensibility.

---

## Contact

**BluDive Technologies**
Email: [info@bludive.com](mailto:info@bludive.com)
Website: [www.bludive.com](https://www.bludive.com)
GitHub: [BluDive GitHub](https://github.com/bludive)

---

*This README covers the complete BluInsights project including all backend services and frontend integration, suitable for production, demonstration, and DevOps POC workflows.*
