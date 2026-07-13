# Minimal Backend Core

A production-ready, lightweight web server built with Python and Flask. This project implements the foundational request-response abstraction loop for distributed systems, serving as Week 1, Task BE-01 for the FlyRank Backend AI Engineering internship.

## Project Overview

This backend provides a clean, professional API infrastructure following Python and Flask best practices. It implements the application factory pattern, uses Blueprint routing for modular organization, and includes comprehensive error handling for production-grade reliability.

## Features

- **Application Factory Pattern**: No global app initialization for better testability and configuration management
- **Blueprint Routing**: Modular route organization using Flask Blueprints
- **Configuration Management**: Environment-based configuration with dedicated config module
- **Global Error Handling**: Graceful JSON error responses for 404 and 500 errors
- **Semantic HTTP Status Codes**: Proper use of HTTP status codes for all responses
- **Production-Ready Structure**: Clean, maintainable directory layout following industry standards

## Project Structure

```
minimal-backend-core/
├── app/
│   ├── __init__.py       # Application factory and error handlers
│   ├── routes.py         # Blueprint with API endpoints
│   └── config.py         # Configuration management
├── run.py                # Main entry point
├── requirements.txt      # Pinned dependencies
└── README.md            # This file
```

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Create Virtual Environment

Create a virtual environment to isolate project dependencies:

**Windows (PowerShell):**
```powershell
python -m venv venv
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
```

**Linux/macOS:**
```bash
python3 -m venv venv
```

### Step 2: Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required packages with their pinned versions:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:

```bash
python run.py
```

The server will start on `http://0.0.0.0:5000` and will be accessible at `http://localhost:5000`.

## API Documentation

### Endpoints Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint with welcome message and API information |
| `/health` | GET | Health check endpoint with service status and assignment details |

### Endpoint Details

#### 1. Root Endpoint

**URL:** `/`  
**Method:** `GET`  
**Description:** Returns a professional welcome message with API version and status.

**Example Request:**
```bash
curl http://localhost:5000/
```

**Example Response (200 OK):**
```json
{
  "message": "Welcome to the Minimal Backend Core API",
  "description": "A production-ready Flask backend implementing the request-response abstraction loop for distributed systems.",
  "api_version": "1.0.0",
  "status": "operational",
  "service": "Minimal Backend Core"
}
```

#### 2. Health Check Endpoint

**URL:** `/health`  
**Method:** `GET`  
**Description:** Returns service health status, infrastructure track, and assignment details.

**Example Request:**
```bash
curl http://localhost:5000/health
```

**Example Response (200 OK):**
```json
{
  "status": "healthy",
  "service": "Minimal Backend Core",
  "infrastructure_track": "Backend AI Engineering",
  "assignment": {
    "code": "BE-01",
    "description": "Week 1, Task BE-01 - Production-ready minimal web server"
  },
  "api_version": "1.0.0",
  "timestamp": "operational"
}
```

### Error Responses

#### 404 Not Found

**Example Request:**
```bash
curl http://localhost:5000/nonexistent
```

**Example Response (404 Not Found):**
```json
{
  "error": "Not Found",
  "message": "The requested resource was not found on this server.",
  "status_code": 404
}
```

#### 500 Internal Server Error

**Example Response (500 Internal Server Error):**
```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred on the server.",
  "status_code": 500
}
```

## Verification Guidelines

Test the API endpoints using `curl` commands:

### Test Root Endpoint
```bash
curl -i http://localhost:5000/
```

### Test Health Endpoint
```bash
curl -i http://localhost:5000/health
```

### Test 404 Error Handling
```bash
curl -i http://localhost:5000/invalid-route
```

Expected response should include `HTTP/1.1 404 NOT FOUND` with JSON error body.

## Configuration

The application uses environment-based configuration. Default settings are defined in `app/config.py`:

- `DEBUG`: Debug mode (default: `False`)
- `TESTING`: Testing mode (default: `False`)
- `API_VERSION`: API version string (default: `'1.0.0'`)
- `APP_NAME`: Application name (default: `'Minimal Backend Core'`)
- `INFRASTRUCTURE_TRACK`: Infrastructure track identifier (default: `'Backend AI Engineering'`)
- `ASSIGNMENT_CODE`: Assignment code (default: `'BE-01'`)

## Production Deployment

For production environments, use a WSGI server like Gunicorn instead of the built-in Flask development server:

**Install Gunicorn:**
```bash
pip install gunicorn
```

**Run with Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

## Best Practices Implemented

- **Application Factory Pattern**: Enables flexible configuration and easier testing
- **Blueprint Architecture**: Modular route organization for scalability
- **Configuration Management**: Centralized settings with environment support
- **Global Error Handling**: Consistent JSON error responses across all endpoints
- **Semantic HTTP Codes**: Proper use of status codes for RESTful API design
- **Dependency Pinning**: Exact versions in requirements.txt for reproducibility
- **Clean Code Structure**: Professional directory layout and code organization
