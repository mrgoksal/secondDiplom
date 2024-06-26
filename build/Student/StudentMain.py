import os
import subprocess
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frameS0'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close():
    window.destroy()
def all_cours():
    window.destroy()
    subprocess.Popen(["Python","AllCoursStudent.py"])
def all_teachers():
    window.destroy()
    subprocess.Popen(["Python","AllTeachers.py"])
def Open_back_form():
    window.destroy()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "..", "Registration", "First.py")
    subprocess.Popen(["python", file_path])
def Complite():
    window.destroy()
    subprocess.Popen(["Python","CompliteTest.py"])

window = Tk()

window.geometry("1600x900")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    800.0,
    453.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=all_cours,
    relief="flat"
)
button_1.place(
    x=609.0,
    y=249.0,
    width=381.0,
    height=90.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=all_teachers,
    relief="flat"
)
button_2.place(
    x=513.0,
    y=360.0,
    width=574.0,
    height=90.0
)

canvas.create_text(
    648.0,
    43.0,
    anchor="nw",
    text="STUDENT",
    fill="#000000",
    font=("Itim Regular", 70 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=close,
    relief="flat"
)
button_3.place(
    x=1333.0,
    y=0.0,
    width=266.98114013671875,
    height=200.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Open_back_form,
    relief="flat"
)
button_4.place(
    x=14.0,
    y=801.804931640625,
    width=300.0,
    height=87.19510650634766
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=Complite,
    relief="flat"
)
button_5.place(
    x=650.0,
    y=492.0,
    width=287.0,
    height=90.0
)
window.resizable(False, False)
window.mainloop()
