# BluInsights User Service (Node.js + Express)

## Overview

The User Service is a backend microservice for managing user authentication and profiles for the BluInsights Tech Blog. It handles user registration, login, JWT authentication, and profile fetching. This service ensures secure access for blog administrators and provides necessary user information to other services.

---

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Folder Structure](#folder-structure)
* [Environment Variables](#environment-variables)
* [Setup & Installation](#setup--installation)
* [Running the Service](#running-the-service)
* [API Endpoints](#api-endpoints)
* [Authentication](#authentication)
* [Error Handling](#error-handling)
* [Notes](#notes)

---

## Features

* User registration with username and password.
* Login functionality with JWT token issuance.
* Profile fetching for authenticated users.
* Passwords securely hashed using bcrypt.
* JWT authentication middleware for route protection.

---

## Tech Stack

* Node.js
* Express.js
* MongoDB or SQLite (POC)
* JWT for authentication
* bcrypt for password hashing
* dotenv for environment configuration

---

## Folder Structure

```
user-service/
│
├── controllers/          # Contains logic for login, register, and profile endpoints
│   ├── authController.js
│   
│
├── routes/               # Express route definitions
│   ├── authRoutes.js
│   
│
├── models/               # User schema
│   └── User.js
│
│
├── .env                  # Environment variables (JWT secret, DB URL, PORT)
├── package.json          # NPM package file
└── app.js             # Entry point for the service
```

---

## Environment Variables

Create a `.env` file in the root folder with the following variables:

```
PORT=5050
DB_URL=<your-database-url>
JWT_SECRET=<your-secret-key>
```

* `PORT`: The port the service will run on.
* `DB_URL`: Database connection string (MongoDB URI or SQLite file path for POC).
* `JWT_SECRET`: Secret key used to sign JWT tokens.

---

## Setup & Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd user-service
```

2. Install dependencies:

```bash
npm install
```

3. Set up `.env` file (see Environment Variables section).

4. Ensure your database (MongoDB or SQLite) is accessible and running.

---

## Running the Service

```bash
npm start
```

or for development with auto-reload:

```bash
npm run dev
```

The service will run on `http://localhost:<PORT>`.

---

## API Endpoints

### Auth Routes

| Method | Endpoint        | Description                      | Body                     | Response                                 |
| ------ | --------------- | -------------------------------- | ------------------------ | ---------------------------------------- |
| POST   | `/api/register` | Register a new user              | `{ username, password }` | `{ message: "Registration successful" }` |
| POST   | `/api/login`    | Authenticate user and return JWT | `{ username, password }` | `{ token: <JWT> }`                       |

### Profile Routes

| Method | Endpoint       | Description                      | Headers                       | Response                            |
| ------ | -------------- | -------------------------------- | ----------------------------- | ----------------------------------- |
| GET    | `/api/profile` | Fetch authenticated user profile | `Authorization: Bearer <JWT>` | `{ user: { username, createdAt } }` |

---

## Authentication

* JWT is used for securing protected routes.
* Upon login, a JWT token is issued to the client.
* The token must be included in the `Authorization` header for accessing profile and other protected endpoints.

Example header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Error Handling

* Returns proper HTTP status codes and messages.
* Common responses:

  * `400 Bad Request` – invalid input.
  * `401 Unauthorized` – invalid or missing JWT.
  * `500 Internal Server Error` – server-side errors.

Example error response:

```json
{
  "error": "Invalid credentials"
}
```

---

## Notes

* For POC, SQLite can be used to simplify setup.
* Passwords must never be stored in plain text.
* Only authenticated users (admins) can access protected routes.
* The service is designed to be modular, allowing integration with the Blog and Comment services seamlessly.

---

This User Service forms the backbone of authentication and authorization for the BluInsights Tech Blog. It can be extended to support multiple admin accounts, role-based access, or integrated with external identity providers if needed.
