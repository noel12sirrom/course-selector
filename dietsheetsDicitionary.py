computer_Science = {
    "lev1Sem1" : """INSERT INTO Courses (course_code, module_name, credits, semester)
    VALUES
    ('CMP1024', 'Programming 1', 4, 1),
    ('CMP1026', 'Computer Networks 1', 3, 1),
    ('INT1001', 'Information Technology', 3, 1),
    ('COM1024', 'Academic Literacy for Undergraduates', 3, 1),
    ('MAT1047', 'College Mathematics 1B', 4, 1),
    ('CSP1001', 'Community Service Project', 1, 1),
    ('CMP1020', 'GET INFO FROM UTECH', 0, 0), --need to be changed
    ('RES3001', 'GET INFORMATION FROM UTECH', 0, 0); --need to be changed""",

    "lev1Sem2" : """INSERT INTO Courses (course_code, module_name, credits, semester)
    VALUES
    ('CMP1025', 'Programming 2', 4, 2),
    ('COM2016', 'Critical Thinking, Reading and Writing', 3, 2),
    ('MAT1008', 'Discrete Mathematics', 4, 2),
    ('PSY1002', 'Introduction to Psychology', 3, 2),
    ('ENS3001', 'Environmental Studies', 3, 2),
    ('MEE2003', 'Material Science', 3, 2);
    """,

    "lev2Sem1" : """INSERT INTO Courses (course_code, module_name, credits, semester)
    VALUES
    ('CIT2004', 'Object Oriented Programming', 4, 1),
    ('STA2020', 'Introductory Statistics', 3, 1),
    ('CIT2011', 'Web Programming', 3, 1),
    ('CMP1005', 'Computer Logic & Digital Design', 3, 1),
    ('CMP2018', 'Database Design', 3, 1);
    """,

    "lev2Sem2" : """INSERT INTO Courses (course_code, module_name, credits, semester, is_elective)
    VALUES
    ('CMP2006', 'Data Structures', 4, 2, FALSE),
    ('CMP2019', 'Software Engineering Analysis & Design', 3, 2, FALSE),
    ('HUM3010', 'Professional Ethics & Legal Implications of Computing Systems', 3, 2, FALSE),
    ('PHS1019', 'Physics for Computer Science', 4, 2, FALSE);
    """,

    "lev3Sem1" : """INSERT INTO Courses (course_code, module_name, credits, semester, is_elective)
    VALUES
    ('CIT3002', 'Operating Systems', 3, 1, FALSE),
    ('CIT4024', 'IT Project Management', 4, 1, FALSE),
    ('CIT3003', 'Analysis of Algorithms', 3, 1, FALSE),
    ('CIT3009', 'Advanced Programming', 3, 1, FALSE),
    ('CMP3040', 'Forensic Computing', 3, 1, TRUE),
    ('BIO3004', 'Introduction to Bioinformatics', 3, 1, TRUE);
    """,

    "lev3Sem2" : """INSERT INTO Courses (course_code, module_name, credits, semester, is_elective)
    VALUES
    ('RES3024', 'Computing Research Methods', 3, 2, FALSE),
    ('CIT3006', 'Theory of Computation', 3, 2, FALSE),
    ('CIT4020', 'Computer Security', 3, 2, FALSE),
    ('MAT2003', 'Calculus 1', 3, 2, FALSE),
    ('STA2016', 'Design of Experiments', 3, 2, FALSE);
    """,

    "lev4Sem1" : """INSERT INTO Courses (course_code, module_name, credits, semester, is_elective)
    VALUES
    ('PRJ4020', 'Major Project (Yearlong project)', 3, 1, FALSE),
    ('CMP3011', 'Computer Organisation and Assembly', 3, 1, FALSE),
    ('CMP4011', 'Artificial Intelligence', 4, 1, FALSE),
    ('MAT1043', 'Linear Algebra', 3, 1, FALSE);
    """,
    
    "lev4Sem2" : """INSERT INTO Courses (course_code, module_name, credits, semester, is_elective)
    VALUES
    ('CIT4036', 'Professional Development Seminar', 1, 2, FALSE),
    ('ENT3001', 'Entrepreneurship', 3, 2, FALSE),
    ('CIT4004', 'Analysis of Programming Languages', 3, 2, FALSE);
    """,
    
    "electives" :"""INSERT INTO Courses (course_code, module_name, credit_hours, semester, is_elective)
    VALUES
    ('CIT3021', 'Foundations of Information Systems', 3, 1, TRUE),
    ('CIT4001', 'Software Implementation', 3, 1, TRUE),
    ('CIT3012', 'Advanced Databases', 4, 1, TRUE),
    ('CIT3013', 'Database Administration', 4, 1, TRUE),
    ('CIT4009', 'Enterprise Computing 1', 4, 1, TRUE),
    ('CIT4010', 'Enterprise Computing 2', 4, 2, TRUE),
    ('CIT3024', 'Enterprise Architecture and Infrastructure', 4, 1, TRUE),
    ('CIT4023', 'E-Business Strategy & E-Commerce', 4, 2, TRUE),
    ('CIT3025', 'IS Innovation and Emerging Technologies', 4, 2, TRUE),
    ('CIT4032', 'IS Strategy, Planning and Management', 4, 2, TRUE),
    ('CIT4031', 'IS Auditing', 4, 1, TRUE),
    ('CIT4033', 'Distributed Systems', 4, 2, TRUE),
    ('CIT3015', 'Digital Communication/Telecommunication', 4, 1, TRUE),
    ('CIT3014', 'Advanced Computer Networks', 4, 2, TRUE),
    ('CIT3017', 'Network Administration & Technical Support', 4, 1, TRUE),
    ('CIT4035', 'Network Management and Security', 4, 2, TRUE),
    ('CIT4034', 'Web Systems Design & Implementation', 4, 2, TRUE),
    ('CIT3023', 'Introduction to Human Computer Interaction', 4, 1, TRUE),
    ('CIT4011', 'Digital Graphics', 4, 1, TRUE),
    ('CIT3020', 'Digital Video Effects', 4, 2, TRUE),
    ('CIT3018', 'Computer Animation', 4, 1, TRUE),
    ('CIT3027', 'Mobile Computing', 4, 1, TRUE),
    ('CMP3041', 'Applied Software Testing', 4, 2, TRUE),
    ('CIT4017', 'Decision Science', 3, 2, TRUE)
    """
}
computer_Science_prerequisites = {
    "lev1Sem2" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('CMP1025', 'CMP1024', NULL, NULL),
    ('COM2016', 'CMP1024', NULL, 'A'),
    ('COM2016', 'COM1020', NULL, 'A'),
    ('MAT1008', 'MAT1047', NULL, NULL)
    """,

    "lev2Sem1" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('CIT2004', 'CMP1025', NULL, NULL),
    ('STA2020', 'MAT1047', NULL, NULL),
    ('CIT2011', 'INT1001', NULL, NULL),
    ('CMP1005', 'INT1001', NULL, NULL),
    ('CMP2018', 'INT1001', NULL, NULL)
    """,

    "lev2Sem2" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('CMP2006', 'CIT2004', NULL, NULL),
    ('CMP2019', 'INT1001', NULL, NULL),
    ('HUM3010', 'CMP2019', NULL, NULL),
    ('HUM3010', 'CMP1020', NULL, 'B'),
    ('HUM3010', 'CMP1024', NULL, 'B'),
    ('PHS1019', 'MAT1008', NULL, 'C'),
    ('PHS1019', 'MAT2003', NULL, 'C')
    """,

    "lev3Sem1" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('CIT3002', 'CMP2006', 'A', NULL),
    ('CIT3002', 'CMP1005', 'A', NULL),
    ('CIT4024', 'INT1001', NULL, NULL),
    ('CIT3003', 'CMP2006', NULL, NULL),
    ('CIT3003', 'MAT2003', NULL, 'D'),
    ('CIT3003', 'MAT1008', NULL, 'D'),
    ('CIT3009', 'CIT3002', 'A', NULL),
    ('BIO3004', 'PHS1019', NULL, NULL)
    """,

    "lev3Sem2" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('RES3024', 'COM1020', NULL, 'E'),
    ('RES3024', 'COM1024', NULL, 'E'),
    ('CIT3006', 'CIT3003', NULL, NULL),
    ('CIT4020', 'CIT3002', NULL, NULL),
    ('CIT4020', 'CMP2018', NULL, NULL),
    ('MAT2003', 'MAT1047', NULL, NULL),
    ('STA2016', 'STA2020', NULL, NULL),
    ('CIT3029', 'LEVEL03', NULL, NULL)--intership
    """,

    "lev4Sem1" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('PRJ4020', 'RES3001', NULL, 'F'),
    ('PRJ4020', 'RES3024', NULL, 'F'),
    ('CMP3011', 'CMP1005', NULL, NULL),
    ('CMP4011', 'CIT3006', NULL, NULL),
    ('MAT1043', 'MAT1047', NULL, NULL)
    """,
    
    "lev4Sem2" : """INSERT INTO Prerequisites (course_code, prerequisite_course_code, corequisite_group, optional_prerequisite_group)
    VALUES
    ('CIT4036', 'LEVEL04', NULL, NULL),
    ('CIT4004', 'CMP4011', NULL, NULL)
    """
}




