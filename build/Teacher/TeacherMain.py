
from pathlib import Path
import subprocess
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frame1'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close_form():
    window.destroy()

def Open_back_form():
    window.destroy()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "..", "Registration", "TeacherAuthoriz.py")
    subprocess.Popen(["python", file_path])

def Open_Setting_Form():
    window.destroy()
    subprocess.Popen(["Python","settings.py"])


def Open_MyCours_Form():
    window.destroy()
    subprocess.Popen(["Python", "MyCoursTeacher.py"])

def Open_AllCours_Form():
    window.destroy()
    subprocess.Popen(["Python", "allcursTeachers.py"])

def Open_Point_Form():
    window.destroy()
    subprocess.Popen(["Python", "PointStudentByTeacher.py"])

def Open_Delete_Form():
    window.destroy()
    subprocess.Popen(["Python", "DeleteCoursTeacher.py"])

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
    800.0,
    450.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1_close = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=close_form,
    relief="flat"
)
button_1_close.place(
    x=1333.0,
    y=0.0,
    width=266.98114013671875,
    height=200.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2_setting = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Open_Setting_Form,
    relief="flat"
)
button_2_setting.place(
    x=128.0,
    y=249.0,
    width=476.0,
    height=90.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3_Delete = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Open_Delete_Form,
    relief="flat"
)
button_3_Delete.place(
    x=128.0,
    y=525.0,
    width=507.0,
    height=90.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4_point = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Open_Point_Form,
    relief="flat"
)
button_4_point.place(
    x=1027.0,
    y=387.0,
    width=287.0,
    height=90.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5_AllCours = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=Open_AllCours_Form,
    relief="flat"
)
button_5_AllCours.place(
    x=679.0,
    y=249.0,
    width=635.0,
    height=90.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6_MyCours = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=Open_MyCours_Form,
    relief="flat"
)
button_6_MyCours.place(
    x=128.0,
    y=387.0,
    width=839.0,
    height=90.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7_back = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=Open_back_form,
    relief="flat"
)
button_7_back.place(
    x=14.0,
    y=801.804931640625,
    width=300.0,
    height=87.19510650634766
)

canvas.create_text(
    637.0,
    39.0,
    anchor="nw",
    text="TEACHER",
    fill="#000000",
    font=("Itim Regular", 70 * -1)
)
window.resizable(False, False)
window.mainloop()
