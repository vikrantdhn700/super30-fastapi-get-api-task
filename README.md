# Super30 FastAPI GET API Task

A beginner-friendly REST API project built with FastAPI. It demonstrates how
to create GET endpoints, return JSON responses, use path parameters, work with
simple student data, and perform basic number operations.

## Project objective

The objective of this project is to learn how to:

- Create and run a FastAPI application
- Build GET API endpoints
- Accept string and integer path parameters
- Return dictionaries and lists as JSON responses
- Perform calculations and conditional logic through an API
- Explore and test endpoints using FastAPI's interactive documentation

## Installation steps

### 1. Open the project directory

```powershell
cd D:\julysuper30\super30-fastapi-get-api-task
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install the dependencies

```powershell
python -m pip install -r requirements.txt
```

## How to run the server

Start the development server with automatic reload:

```powershell
uvicorn main:app --reload
```

Alternatively, run the Python file directly:

```powershell
python main.py
```

The server runs at:

```text
http://127.0.0.1:8000
```

Stop the server by pressing `Ctrl+C` in the terminal.

## Available API endpoints

All application endpoints use the `GET` method.

| Endpoint | Description |
| --- | --- |
| `/` | Returns a welcome message |
| `/students` | Returns all students |
| `/student/{student_id}` | Finds a student using an ID such as `stu1` |
| `/course/` | Returns course details and topics |
| `/skill/` | Returns a list of technical skills |
| `/add/{number1}/{number2}` | Adds two integers |
| `/multiply/{number1}/{number2}` | Multiplies two integers |
| `/square/{number}` | Calculates the square of an integer |
| `/check/{number}` | Checks whether an integer is even or odd |
| `/age/{age}` | Returns the age category for a supplied age |
| `/table/{number}` | Generates a multiplication table from 1 to 10 |
| `/profile/{username}/{age}` | Returns a username and age profile |
| `/number/{number}` | Returns a number's square, cube, and even status |

FastAPI also provides automatic API documentation:

| Documentation | URL |
| --- | --- |
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

## Example URLs

Open these URLs in a browser after starting the server:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/students
http://127.0.0.1:8000/student/stu1
http://127.0.0.1:8000/course/
http://127.0.0.1:8000/skill/
http://127.0.0.1:8000/add/10/5
http://127.0.0.1:8000/multiply/6/7
http://127.0.0.1:8000/square/9
http://127.0.0.1:8000/check/12
http://127.0.0.1:8000/age/25
http://127.0.0.1:8000/table/5
http://127.0.0.1:8000/profile/Vikrant/25
http://127.0.0.1:8000/number/4
```

Example response from `/number/4`:

```json
{
  "number": 4,
  "square": 16,
  "cube": 64,
  "even": true
}
```

## Project structure

```text
super30-fastapi-get-api-task/
|-- main.py          # FastAPI application and GET endpoints
|-- requirements.txt # Project dependencies
`-- README.md        # Project documentation
```

## Author/student name

**Vikrant Kumar**

## Submission

The submission includes:

- The complete FastAPI source code in `main.py`
- All required dependencies in `requirements.txt`
- Installation and usage documentation in `README.md`
- GET endpoints for student data, course information, skills, profiles, age
  categories, and mathematical operations
- Interactive Swagger UI for testing and verifying every endpoint
