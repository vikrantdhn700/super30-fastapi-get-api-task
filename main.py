import uvicorn
from fastapi import FastAPI


app = FastAPI()

""" Home API endpoint """


@app.get("/")
def home():
    return {"message": "Welcome to Super30 FastAPI"}


""" Students API endpoint """


@app.get("/students")
def get_students():
    students = [
        {"student_id": "stu1", "name": "Alice",
            "batch": "super30", "role": "student"},
        {"student_id": "stu2", "name": "Bob",
            "batch": "super30", "role": "student"},
        {"student_id": "stu3", "name": "Charlie",
            "batch": "super30", "role": "student"},
    ]
    return {"students": students}


@app.get("/student/{student_id}")
def get_student(student_id: str):
    students = [
        {"student_id": "stu1", "name": "Alice",
            "batch": "super30", "role": "student"},
        {"student_id": "stu2", "name": "Bob",
            "batch": "super30", "role": "student"},
        {"student_id": "stu3", "name": "Charlie",
            "batch": "super30", "role": "student"},
    ]
    student = next(
        (s for s in students if s["student_id"] == student_id), None)
    return {"student": student}


""" Course API endpoint """


@app.get("/course/")
def get_course():
    return {
        "course_name": "Backend Development with FastAPI",
        "mentor": "Sudhanshu",
        "duration": "8 Weeks",
        "topics": [
            "Python",
            "FastAPI",
            "REST API",
            "Database",
            "Deployment"
        ]
    }


""" Skills API endpoint """


@app.get('/skills/')
def get_skill():
    return {
        "skills": [
            "Python",
            "FastAPI",
            "REST API",
            "Database",
            "Deployment",
            "SQL",
            "Docker",
            "AWS"
        ]
    }


""" Additional API endpoint """


@app.get("/add/{number1}/{number2}")
def add_numbers(number1: int, number2: int):
    result = number1 + number2
    return {"result": result}


""" Multiply API endpoint """


@app.get("/multiply/{number1}/{number2}")
def multiply_numbers(number1: int, number2: int):
    result = number1 * number2
    return {"result": result}


""" Square API endpoint """


@app.get("/square/{number}")
def square_number(number: int):
    result = number * number
    return {"number": number, "result": result}


""" Even or Odd API endpoint """


@app.get("/check/{number}")
def even_odd_number(number: int):
    if number % 2 == 0:
        return {"number": number, "type": "even"}
    else:
        return {"number": number, "type": "odd"}


""" Age API endpoint """


@app.get("/age/{age}")
def check_age(age: int):
    if age >= 4 and age <= 12:
        return {"age": age, "message": "You are a child"}
    elif age >= 13 and age <= 19:
        return {"age": age, "message": "You are a teenager"}
    elif age >= 20 and age <= 59:
        return {"age": age, "message": "You are an adult"}
    elif age >= 60:
        return {"age": age, "message": "You are a senior citizen"}
    else:
        return {"age": age, "message": "You are a kid"}


""" Multiplication Table API endpoint """


@app.get("/table/{number}")
def multiplication_table(number: int):
    table = []
    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")
    return {
        "number": number,
        "table": table
    }


""" Profile API endpoint """


@app.get("/profile/{username}/{age}")
def get_profile(username: str, age: int):
    return {
        "username": username,
        "age": age
    }


""" Number Analysis API endpoint """


@app.get("/number/{number}")
def check_number(number: int):
    square_num = number * number
    cube_num = number * number * number
    if number % 2 == 0:
        even = True
    else:
        even = False

    return {
        "number": number,
        "square": square_num,
        "cube": cube_num,
        "even": even
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
