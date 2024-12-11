#from multiprocessing import connection
from database import get_connection
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

import funcs

app = FastAPI()

class Course(BaseModel):
    course_code: str
    module_name: str
    credits: int
    semester: int
    is_elective: bool 
       
@app.get("/")
async def root():
    return {"server is up and running with ovicron"}

@app.get("/modules")
async def get_modules():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM courses LEFT JOIN prerequisites ON courses.course_code = prerequisites.course_code")
        modules = cursor.fetchall()
        return funcs.parse_modules(modules) # Return as a list of module names with prerequisites
    finally:
        connection.close()  # Ensure connection is closed

@app.get("/modules/{module_code}")
def getModuleDetail(module_code:str):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM courses WHERE course_code = ?",(module_code,)),
        rows = cursor.fetchall()
        return [dict(zip([col[0] for col in cursor.description], row)) for row in rows]  # Convert rows to dicts
    finally:
        connection.close()

@app.post("/modules/addcourse")
async def add_course(course: Course):
    connection = get_connection()
    cursor = connection.cursor()
    try:    
        #Insert course into the database
        cursor.execute(
            "INSERT INTO courses (course_code, module_name, credits, semester, is_elective) VALUES (?, ?, ?, ?, ?)",
            (course.course_code, course.module_name, course.credits, course.semester, course.is_elective),
        )
        connection.commit()
        return {"message": f"Course {course.module_name} added successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Course code already exists")
    finally:
        connection.close()
