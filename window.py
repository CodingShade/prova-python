from tkinter import *
import pywhatkit as kit
from datetime import datetime, timedelta


def btn_clicked():
    numero = entry0.get()
    if not numero.startswith('+'):
        numero = '+55' + numero
    mensagem = entry2.get("1.0", "end-1c")

    # Obter o horário atual e adicionar 2 minutos
    agora = datetime.now() + timedelta(minutes=1)
    hora = agora.hour
    minuto = agora.minute

    kit.sendwhatmsg(numero, mensagem, hora, minuto)
    print(f"Mensagem enviada para {numero} às {hora}:{minuto} com a mensagem: {mensagem}")

window = Tk()

window.geometry("800x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    400.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    231.5, 229.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 46.0, y = 205,
    width = 371.0,
    height = 46)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    399.5, 430.0,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 49.0, y = 335,
    width = 701.0,
    height = 188)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 192, y = 541,
    width = 387,
    height = 48)

canvas.create_text(
    519.5, 570.5,
    text = "Enviar",
    fill = "#000000",
    font = ("None", int(32.0)))

window.resizable(False, False)
window.mainloop()
