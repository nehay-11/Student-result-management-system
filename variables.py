from tkinter import StringVar


def create_variables(root):
    variables = {
        "name_var": StringVar(root),
        "roll_var": StringVar(root),
        "course_var": StringVar(root),
        "mark1_var": StringVar(root),
        "mark2_var": StringVar(root),
        "mark3_var": StringVar(root)
    }

    return variables