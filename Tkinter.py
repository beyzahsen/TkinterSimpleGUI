from tkinter import * 
import tkinter.font as font


window = Tk()

window.title("Adres Gezgini")
window.geometry("903x628")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#F8C471",
    height = 628,
    width = 903,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)
canvas.create_text(
    37.0,
    29.0,
    anchor="nw",
    text="Anahtar Kelimeler",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    440.0,
    29.0,
    anchor="nw",
    text="Hata & Uyarılar",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_1 = Button(
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    bg="#2E86C1",
    text="Eşleştir",
    border =2,
    font=20
)

button_1.place(
    x=200.0,
    y=470.0,
    width=400.0,
    height=42.0

)

button_2 = Button(
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    bg= "#E74C3C",
    text="Önbelliği Temizle",
    border=2,
    font=10
)
button_2.place(
    x=501.0,
    y=520.0,
    width=208.0,
    height=33.0
)


entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    border = 2
)
entry_1.place(
    x=47.0,
    y=78.0,
    width=265.0,
    height=355.0
)


entry_2 = Text(
    bd=0,
    bg= "#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    border = 2
)

entry_2.bind("<Key>", lambda e: "break")

entry_2.place(
    x=449.0,
    y=78.0,
    width=265.0,
    height=355.0
)


def retrive_input(inputValue):
    inputValue = entry_1.get("1.0","end-1c")
    return inputValue


window.resizable(False, False)
window.mainloop()