from tkinter import *
from variables import create_variables
from ui import build_ui


root = Tk()
root.title("Student Result Management System")
root.geometry("1000x600")
root.config(bg="white")


variables = create_variables(root)

build_ui(root, variables)

root.mainloop()