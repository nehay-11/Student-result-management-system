# Student Result Management System
A simple desktop-based Student Result Management System developed using Python, Tkinter, and MySQL with CRUD operations and GUI interface.

## Features
- Add student records
- Update student details
- Delete records
- View all student results
- Automatic percentage calculation
- Automatic grade generation
- MySQL database connectivity
- Simple GUI using Tkinter

## Technologies Used
- Python
- Tkinter
- MySQL
- mysql-connector-python

## Project Structure

student_result_system/
│
├── main.py
├── db.py
├── functions.py
├── ui.py
├── variables.py
└── README.md

## Database Setup
Run the following SQL queries in MySQL:
CREATE DATABASE student_result_system;
USE student_result_system;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    roll_no VARCHAR(20),
    course VARCHAR(50),
    marks1 INT,
    marks2 INT,
    marks3 INT,
    total INT,
    percentage FLOAT,
    grade VARCHAR(10)
);
