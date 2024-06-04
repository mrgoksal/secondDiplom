
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


REGISTRATION_PATH = Path(__file__).resolve().parent
ASSETS_PATH = REGISTRATION_PATH.parent / 'Main' / 'frameS5'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1333.0,
    y=0.0,
    width=266.98114013671875,
    height=200.0
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
    732.0,
    108.0,
    anchor="nw",
    text="Оценка",
    fill="#000000",
    font=("Kyiv*Type Titling", 35 * -1)
)

canvas.create_text(
    284.0,
    288.0,
    anchor="nw",
    text="Оценка",
    fill="#000000",
    font=("Kyiv*Type Titling", 35 * -1)
)

canvas.create_text(
    954.0,
    238.0,
    anchor="nw",
    text="Место для заметки",
    fill="#000000",
    font=("Kyiv*Type Titling", 35 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1128.5,
    449.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=823.0,
    y=280.0,
    width=611.0,
    height=337.0
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
    x=130.1835594177246,
    y=672.0,
    width=45.63333511352539,
    height=74.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    352.0,
    450.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=238.0,
    y=336.0,
    width=228.0,
    height=226.0
)

canvas.create_text(
    648.0,
    43.0,
    anchor="nw",
    text="STUDENT",
    fill="#000000",
    font=("Itim Regular", 70 * -1)
)
window.resizable(False, False)
window.mainloop()
