# FastAPI Authentication API

This project is a backend API built while learning FastAPI.
It focuses on authentication, authorization, and database-backed APIs.

The project is implemented step by step while following a FastAPI course,
with an emphasis on understanding how things work internally.

## Features Implemented

- FastAPI project structure with routers
- PostgreSQL database integration
- SQLAlchemy ORM models
- Pydantic schemas for request/response validation
- User registration
- Password hashing and verification
- OAuth2 password-based login
- JWT access token generation (HS256)
- Token expiration handling
- Verifying logged-in users using JWT
- Protecting routes using OAuth2 and JWT

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- OAuth2 (Password Flow)
- JWT (HS256)
- python-jose
- python-dotenv

## Authentication Flow

1. User registers with email and password
2. Password is hashed before storing in the database
3. User logs in using OAuth2 password flow
4. Server validates credentials
5. Server generates a JWT containing user_id
6. Client sends token in Authorization header
7. Protected routes verify the token and extract user information

## Environment Variables

This project uses environment variables for sensitive configuration.

Create a `.env` file in the project root:

DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fastapi

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


⚠️ The `.env` file is ignored and not committed to GitHub.

## How to Run

1. Create and activate a virtual environment
2. Install dependencies
3. Set up PostgreSQL
4. Add `.env` file
5. Run the server

## uvicorn app.main:app --reload


## Current Status

Authentication and authorization are implemented.
The project will be extended with additional features
such as relationships, voting, testing, and deployment.

## Notes

This is a learning project.
Code is written while studying FastAPI concepts and best practices.


Built while learning backend development with FastAPI.
