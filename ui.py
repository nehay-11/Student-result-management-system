from tkinter import *
from tkinter import ttk
from functions import add_student, show_students

def build_ui(root, vars):

    heading = Label(
        root,
        text="Student Result Management System",
        font=("Arial", 20, "bold"),
        bg="navy",
        fg="white"
    )

    heading.pack(fill=X)
    form_frame = Frame(root, bg="white")
    form_frame.place(x=20, y=60, width=300, height=500)

    Label(form_frame, text="Student Name", bg="white").place(x=20, y=20)
    Entry(form_frame, textvariable=vars["name_var"]).place(x=20, y=50)

    Label(form_frame, text="Roll No", bg="white").place(x=20, y=90)
    Entry(form_frame, textvariable=vars["roll_var"]).place(x=20, y=120)

    Label(form_frame, text="Course", bg="white").place(x=20, y=160)
    Entry(form_frame, textvariable=vars["course_var"]).place(x=20, y=190)

    Label(form_frame, text="Marks 1", bg="white").place(x=20, y=230)
    Entry(form_frame, textvariable=vars["mark1_var"]).place(x=20, y=260)

    Label(form_frame, text="Marks 2", bg="white").place(x=20, y=300)
    Entry(form_frame, textvariable=vars["mark2_var"]).place(x=20, y=330)

    Label(form_frame, text="Marks 3", bg="white").place(x=20, y=370)
    Entry(form_frame, textvariable=vars["mark3_var"]).place(x=20, y=400)

    table_frame = Frame(root)
    table_frame.place(x=340, y=60, width=630, height=500)

    student_table = ttk.Treeview(table_frame)
    student_table['columns'] = (
        "id",
        "name",
        "roll",
        "course",
        "m1",
        "m2",
        "m3",
        "total",
        "percentage",
        "grade"
    )
    student_table.column("#0", width=0, stretch=NO)

    for col in student_table['columns']:
        student_table.column(col, width=80)
        student_table.heading(col, text=col)


    student_table.pack(fill=BOTH, expand=1)

    Button(
        form_frame,
        text="Add",
        bg="green",
        fg="white",
        command=lambda: add_student(vars, student_table)
    ).place(x=20, y=450, width=80)
    show_students(student_table)

