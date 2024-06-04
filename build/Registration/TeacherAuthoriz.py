from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frame16'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close_form():
    window.destroy()

def Open_back_form():
    window.destroy()
    subprocess.Popen(["Python","First.py"])

def Open_registr_form():
    window.destroy()
    subprocess.Popen(["Python","Registration_Teacher.py"])


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
    text="Authorization",
    fill="#000000",
    font=("IrishGrover Regular", 65 * -1)
)

canvas.create_text(
    683.0,
    162.0,
    anchor="nw",
    text="Teacher",
    fill="#000000",
    font=("IrishGrover Regular", 65 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    800.0,
    660.0,
    image=entry_image_1
)
entry_1_Password = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20),
    show="*"
)
entry_1_Password.place(
    x=514.0,
    y=589.0,
    width=572.0,
    height=140.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    800.0,
    384.0,
    image=entry_image_2
)
entry_2_login = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Helvetica", 20)
)
entry_2_login.place(
    x=514.0,
    y=313.0,
    width=572.0,
    height=140.0
)

canvas.create_text(
    738.0,
    259.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

canvas.create_text(
    699.0,
    490.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("IrishGrover Regular", 45 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=717.0,
    y=766.0,
    width=157.0,
    height=32.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3_registration = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Open_registr_form,
    relief="flat"
)
button_3_registration.place(
    x=639.0,
    y=832.0,
    width=313.0,
    height=32.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4_back = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Open_back_form,
    relief="flat"
)
button_4_back.place(
    x=14.0,
    y=801.804931640625,
    width=300.0,
    height=87.19510650634766
)

window.resizable(False, False)
window.mainloop()
