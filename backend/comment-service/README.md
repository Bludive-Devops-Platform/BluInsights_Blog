# BluInsights Comment Service

## Overview
The **Comment Service** is a lightweight backend microservice built with **Go** and the **Gin** framework. It manages user comments for blog posts, providing endpoints to create and fetch comments. Each comment is associated with a specific blog post and includes user information and a timestamp.

This service is designed to work seamlessly with the **BluInsights Blog Service** and **User Service**, forming part of a microservices-based architecture for a modern tech blog platform.

---

## Features
- Create comments for a blog post
- Retrieve all comments for a specific blog post
- Store comment text, user ID, and timestamp
- Fast, lightweight, and production-ready Go microservice
- Designed for easy integration with frontend and other backend services

---

## Technology Stack
- **Programming Language:** Go (Golang)
- **Web Framework:** Gin
- **ORM:** GORM
- **Database:** SQLite (POC), can be replaced with PostgreSQL/MySQL for production
- **Port:** `5002` (default)

---

## Project Structure

```

comment-service/
├── controllers/
│   └── comment.go      # Logic for handling GET/POST comment requests
├── models/
│   └── comment.go      # Comment model/schema for GORM
├── routes/
│   └── comment.go      # Defines API routes for comments
├── main.go             # Service entry point
├── go.mod              # Go module file
└── go.sum              # Go dependency checksum file

````

---

## API Endpoints

### 1. Get Comments
- **Endpoint:** `GET /comments/:postId`
- **Description:** Retrieve all comments for a given blog post, ordered by newest first.
- **Request Parameters:**
  - `postId` (path) – The ID of the blog post
- **Response:**
```json
[
  {
    "id": 1,
    "post_id": 2,
    "user_id": "JaneDoe",
    "text": "Great article!",
    "created_at": "2025-10-03T12:34:56Z"
  },
  {
    "id": 2,
    "post_id": 2,
    "user_id": "JohnSmith",
    "text": "Very informative.",
    "created_at": "2025-10-03T12:40:12Z"
  }
]
````

---

### 2. Add Comment

* **Endpoint:** `POST /comments/:postId`
* **Description:** Add a new comment to a blog post.
* **Request Parameters:**

  * `postId` (path) – The ID of the blog post
  * Request body (JSON):

```json
{
  "user_id": "JaneDoe",
  "text": "This is my comment."
}
```

* **Response:**

```json
{
  "id": 3,
  "post_id": 2,
  "user_id": "JaneDoe",
  "text": "This is my comment.",
  "created_at": "2025-10-03T13:00:00Z"
}
```

---

## Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-org/comment-service.git
cd comment-service
```

2. **Install Go Dependencies**

```bash
go mod tidy
```

3. **Run the Service**

```bash
go run main.go
```

* The service will start on `http://localhost:5002`.

4. **Database**

* SQLite database file is created automatically in `database/comment.db`.
* Auto-migration is handled via GORM when the service starts.

---

## Development Notes

* **Controllers:** All API logic is handled in `controllers/comment.go`.
* **Routes:** Defined in `routes/comment.go` to keep endpoints modular.
* **Models:** `models/comment.go` defines the `Comment` struct for GORM.
* **CORS Middleware:** Added in `main.go` to allow cross-origin requests from the frontend.

---

## Integration with Frontend

* Comments can be fetched and posted using AJAX/fetch requests from the frontend.
* Example fetch request for posting a comment:

```javascript
fetch(`http://localhost:5002/comments/${postId}`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ user_id: 'Admin', text: 'Great post!' })
});
```

* Example fetch request for getting comments:

```javascript
fetch(`http://localhost:5002/comments/${postId}`)
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## Error Handling

* **GET /comments/:postId**

  * Returns `500` with JSON `{ "error": "message" }` if there is a database failure.

* **POST /comments/:postId**

  * Returns `400` if `user_id` or `text` is missing in the request body.
  * Returns `500` if there is a database failure.

---

## Author & Maintainers

* **Organization:** BluDive Technologies

---

## License

This project is licensed under the MIT License.


