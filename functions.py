from tkinter import messagebox
from db import connect_db



def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return total, percentage, grade

def clear_fields(vars):
    vars["name_var"].set("")
    vars["roll_var"].set("")
    vars["course_var"].set("")
    vars["mark1_var"].set("")
    vars["mark2_var"].set("")
    vars["mark3_var"].set("")



def add_student(vars, table):
    try:
        m1 = int(vars["mark1_var"].get())
        m2 = int(vars["mark2_var"].get())
        m3 = int(vars["mark3_var"].get())

        total, percentage, grade = calculate_result(m1, m2, m3)

        conn = connect_db()
        cursor = conn.cursor()
        query = """
        INSERT INTO students
        (name, roll_no, course, marks1, marks2, marks3, total, percentage, grade)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            vars["name_var"].get(),
            vars["roll_var"].get(),
            vars["course_var"].get(),
            m1,
            m2,
            m3,
            total,
            percentage,
            grade
        )

        cursor.execute(query, values)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Student added")
        show_students(table)
        clear_fields(vars)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_students(table):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    table.delete(*table.get_children())

    for row in rows:
        table.insert("", "end", values=row)

    conn.close()