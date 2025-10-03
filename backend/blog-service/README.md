# BluInsights Blog Service

## Overview

The **Blog Service** is a core component of the BluInsights platform, responsible for managing all blog-related operations. It handles creating, reading, updating, and deleting blog posts. Each blog post contains the title, content, tags, header image, author, and timestamp. The service is designed to serve JSON responses for easy consumption by the frontend application.

This service is implemented using **FastAPI** with **SQLite** for POC purposes. Header images are stored locally and served via a static endpoint.

---

## Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Folder Structure](#folder-structure)  
- [Setup & Installation](#setup--installation)  
- [Environment Variables](#environment-variables)  
- [Database](#database)  
- [API Endpoints](#api-endpoints)  
- [Usage](#usage)  
- [Testing](#testing)  
- [Future Improvements](#future-improvements)  

---

## Features

- **Create Blog Posts**: Admins can create posts with title, content, tags, and a header image.  
- **Read Blog Posts**: Retrieve all posts or a specific post by ID.  
- **Update Blog Posts**: Edit existing posts.  
- **Delete Blog Posts**: Remove posts when needed.  
- **Image Handling**: Header images are uploaded and served via a static URL.  
- **JSON API**: Fully RESTful, JSON-based responses for frontend consumption.  
- **Author Attribution**: Each post stores the author’s name for tracking.  

---

## Tech Stack

- **Backend Framework**: FastAPI  
- **Database**: SQLite (for POC, can be upgraded to PostgreSQL/MySQL)  
- **ORM**: SQLAlchemy  
- **File Handling**: Local filesystem for header images  
- **API Server**: Uvicorn  
- **Middleware**: CORS via FastAPI middleware  

---

## Folder Structure

```

blog-service/
│
├─ app/
│  ├─ main.py           # Entry point for the FastAPI server
│  ├─ models.py         # SQLAlchemy models
│  ├─ schemas.py        # Pydantic schemas for request/response validation
│  ├─ crud.py           # CRUD operations for the Blog
│
├─ database/            # SQLite database file
├─ images/              # Uploaded blog header images
├─ venv/                # Python virtual environment
├─ requirements.txt     # Python dependencies
└─ README.md

````

---

## Setup & Installation

1. **Clone the repository**

```bash
git clone <repo_url>
cd blog-service
````

2. **Create a Python virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the server**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 5001
```

The server will start at `http://localhost:5001`.

---

## Environment Variables

For POC purposes, this service currently uses local SQLite and default ports. In production, environment variables can be added for:

* `DATABASE_URL` → URL for production DB (PostgreSQL/MySQL)
* `IMAGE_DIR` → Path to store uploaded images
* `SERVER_HOST` → Host IP
* `SERVER_PORT` → Port number

---

## Database

* **Type**: SQLite
* **File Location**: `./database.db`
* **Schema**:

**BlogPost Table**

| Column     | Type     | Description                |
| ---------- | -------- | -------------------------- |
| id         | Integer  | Auto-increment primary key |
| title      | String   | Title of the blog post     |
| content    | Text     | Blog content               |
| tags       | String   | Comma-separated tags       |
| author     | String   | Author's name              |
| image_url  | String   | URL for the header image   |
| created_at | DateTime | Timestamp of creation      |

---

## API Endpoints

### Create Blog Post

```
POST /blogs
Content-Type: multipart/form-data
```

**Form Data:**

| Field   | Type   | Required |
| ------- | ------ | -------- |
| title   | string | yes      |
| content | string | yes      |
| tags    | string | no       |
| author  | string | no       |
| image   | file   | no       |

**Response:**

```json
{
  "id": 1,
  "title": "My First Blog",
  "content": "Content of the blog",
  "tags": "DevOps, Cloud",
  "author": "Admin",
  "image_url": "http://localhost:5001/images/blog-image.png",
  "created_at": "2025-10-01T12:00:00"
}
```

---

### Read All Blog Posts

```
GET /blogs
```

**Query Parameters:**

* `skip` (optional): Number of records to skip
* `limit` (optional): Number of records to return

**Response:** Array of blog objects.

---

### Read Single Blog Post

```
GET /blogs/{blog_id}
```

**Response:** Blog object by ID.

---

### Update Blog Post

```
PUT /blogs/{blog_id}
Content-Type: multipart/form-data
```

**Form Data:** Same as create endpoint

**Response:** Updated blog object

---

### Delete Blog Post

```
DELETE /blogs/{blog_id}
```

**Response:**

```json
{
  "detail": "Blog deleted successfully"
}
```

---

## Usage

1. Upload a blog post with an optional header image.
2. Retrieve posts in descending order (latest first).
3. Update or delete posts using their `id`.
4. Images are served via `http://localhost:5001/images/{filename}` for frontend rendering.

---

## Testing

* Use tools like **Postman** or **cURL** to test all endpoints.
* Ensure the `images/` folder has correct read/write permissions.
* Validate CRUD operations from the frontend integration.

---

## Future Improvements

* Migrate from SQLite to PostgreSQL or MySQL for production.
* Add authentication/authorization for admin-only blog management.
* Implement pagination, filtering by tags/categories, and search.
* Add Markdown support for blog content.
* Integrate cloud storage (AWS S3, GCP, Azure Blob) for images.
* Add API versioning for future compatibility.

---

## License

MIT License

---

## Author

**BluDive Technologies** - Developer Team

```
BluInsights Blog Service | FastAPI | SQLite | RESTful API
```

```

