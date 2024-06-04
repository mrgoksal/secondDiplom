from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frame14'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close_form():
    window.destroy()

def Open_back_form():
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

canvas.create_text(
    600.0,
    100.0,
    anchor="nw",
    text="Registration",
    fill="#000000",
    font=("IrishGrover Regular", 65 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    392.0,
    344.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20)
)
entry_1.place(
    x=106.0,
    y=273.0,
    width=572.0,
    height=140.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    796.0,
    729.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20)
)
entry_2.place(
    x=510.0,
    y=658.0,
    width=572.0,
    height=140.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1189.0,
    344.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20)
)
entry_3.place(
    x=903.0,
    y=273.0,
    width=572.0,
    height=140.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    392.0,
    548.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20)
)
entry_4.place(
    x=106.0,
    y=477.0,
    width=572.0,
    height=140.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    1189.0,
    548.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20)
)
entry_5.place(
    x=903.0,
    y=477.0,
    width=572.0,
    height=140.0
)

canvas.create_text(
    345.0,
    225.0,
    anchor="nw",
    text="Имя",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

canvas.create_text(
    1087.0,
    219.0,
    anchor="nw",
    text="Фамилия",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

canvas.create_text(
    334.0,
    415.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

canvas.create_text(
    742.0,
    604.0,
    anchor="nw",
    text="MAIL",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

canvas.create_text(
    1093.0,
    424.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2_back = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Open_back_form,
    relief="flat"
)
button_2_back.place(
    x=14.0,
    y=801.804931640625,
    width=300.0,
    height=87.19510650634766
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1273.0,
    y=800.0,
    width=300.0,
    height=87.19510650634766
)
window.resizable(False, False)
window.mainloop()