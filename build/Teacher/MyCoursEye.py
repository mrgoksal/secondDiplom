
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frame12'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1333.0,
    y=0.0,
    width=266.98114013671875,
    height=200.0
)

canvas.create_text(
    637.0,
    39.0,
    anchor="nw",
    text="TEACHER",
    fill="#000000",
    font=("Itim Regular", 70 * -1)
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
    x=14.0,
    y=801.804931640625,
    width=300.0,
    height=87.19510650634766
)

canvas.create_text(
    752.0,
    143.0,
    anchor="nw",
    text="Курс: ",
    fill="#000000",
    font=("Kyiv*Type Titling", 35 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1112.5,
    465.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=807.0,
    y=296.0,
    width=611.0,
    height=337.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    342.0,
    256.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=229.5,
    y=217.0,
    width=225.0,
    height=77.0
)

canvas.create_rectangle(
    156.4541015625,
    250.5,
    176.5001220703125,
    261.5,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
