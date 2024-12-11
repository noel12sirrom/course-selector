import sqlite3
from dietsheetsDicitionary import computer_Science, computer_Science_prerequisites

def get_connection():
    conn = sqlite3.connect("Courses.db")
    return conn

courses  = """CREATE TABLE IF NOT EXISTS
courses(course_code VARCHAR PRIMARY KEY, module_name VARCHAR, credits INT NOT NULL, semester INTEGER NOT NULL, is_elective BOOLEAN NOT NULL DEFAULT FALSE)"""

prerequisites  = """CREATE TABLE IF NOT EXISTS
Prerequisites(course_code VARCHAR(10) NOT NULL, prerequisite_course_code VARCHAR(10) NOT NULL, corequisite_group CHAR(3) DEFAULT NULL, optional_prerequisite_group CHAR(3) DEFAULT NULL,
PRIMARY KEY (course_code, prerequisite_course_code),
FOREIGN KEY (course_code) REFERENCES courses(course_code),
FOREIGN KEY (prerequisite_course_code) REFERENCES Courses(course_code))"""

def runQuery():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute()
        connection.commit()
        print("Done!")
    finally:
        connection.close()

#runQuery()    
"""premade querys"""
'''
"UPDATE courses SET is_elective = ? WHERE is_elective IS NULL", (False,)


 for key, value in computer_Science_prerequisites.items():
            cursor.execute(value)

'''