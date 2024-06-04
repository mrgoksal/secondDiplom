
from pathlib import Path
from tkinter import *
from tkinter import messagebox
import subprocess
import sys

# Добавляем путь к модулю db.py в sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'bd'))

# Импортируем функции из db.py
from db import get_connection, execute_query

# Импортируем функции из db.py
from db import execute_query
REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frame0'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close_form():
    window.destroy()

def Open_teacher_form():
    window.destroy()
    subprocess.Popen(["Python","TeacherAuthoriz.py"])

def Open_student_form():
    window.destroy()
    subprocess.Popen(["Python","StudentAuthoriz.py"])

window = Tk()

window.geometry("1600x900")
window.configure(bg = "#FFFFFF")
window.lift()

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
    812.0,
    554.0,
    image=image_image_1
)

button_Close = PhotoImage(
    file=relative_to_assets("button_1.png"))
Close_Button = Button(
    image=button_Close,
    borderwidth=0,
    highlightthickness=0,
    command=close_form,
    relief="flat"
)
Close_Button.place(
    x=1333.0,
    y=0.0,
    width=266.98114013671875,
    height=200.0
)

canvas.create_text(
    600.0,
    100.0,
    anchor="nw",
    text="Authorization",
    fill="#000000",
    font=("IrishGrover Regular", 65 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2_Teacher = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Open_teacher_form,
    relief="flat"
)
button_2_Teacher.place(
    x=600.0,
    y=493.0,
    width=392.0,
    height=123.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3_Student = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Open_student_form,
    relief="flat"
)
button_3_Student.place(
    x=600.0,
    y=284.0,
    width=392.0,
    height=123.0
)

window.resizable(False, False)
window.mainloop()
