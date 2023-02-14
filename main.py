import random
import customtkinter
from PIL import Image
import tkinter
import pygame
from string import ascii_letters

customtkinter.set_appearance_mode('dark') # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme('green') # Themes: "blue" (standard), "green", "dark-blue"

chars = ascii_letters
symbol = '*#$%+'

chars = list(chars + chars.upper() + symbol)


def generate():
    len_password = int(entry_len.get())
    count_password = int(entry_count.get())
    for i in range(count_password):
        password = ''
        for j in range(len_password):
            password += random.choice(chars)
        text_field.insert(tkinter.END, password + '\n')


def clear():
    text_field.delete(0.0, tkinter.END)


pygame.mixer.init()


def play():
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()

window = customtkinter.CTk()
window.geometry('600x600')
window.title('generator')
window.resizable(False, False)

logo = customtkinter.CTkImage(dark_image=Image.open('img.png'), size=(300, 90))
logo_label = customtkinter.CTkLabel(master=window, text='', image=logo)
logo_label.place(x=20, y=10)
# logo1 = customtkinter.CTkImage(dark_image=Image.open('img1.png'), size=(100, 100))
# logo_label1 = customtkinter.CTkLabel(master=window, text='', image=logo1)
# logo_label1.place(x=450, y=10)

customtkinter.CTkLabel(window, text='NUMBER OF PASSWORDS   >  >  >').place(x=170, y=120)
entry_count = customtkinter.CTkEntry(window, width=50)
entry_count.place(x=400, y=120)

customtkinter.CTkLabel(window, text='PASSWORD LENGTH   >  >  >').place(x=170, y=150)
entry_len = customtkinter.CTkEntry(window, width=50)
entry_len.place(x=400, y=150)

btn_generate = customtkinter.CTkButton(window, text='GENERATE', command=generate)
btn_generate.place(x=330, y=190)

btn_clear = customtkinter.CTkButton(window, text='CLEAR', command=clear)
btn_clear.place(x=130, y=190)

btn_play = customtkinter.CTkButton(window, width=10, text='SOUNDon', command=play)
btn_play.place(x=430, y=560)

btn_stop = customtkinter.CTkButton(window, width=10, text='SOUNDoff', command=stop)
btn_stop.place(x=500, y=560)

text_field = customtkinter.CTkTextbox(window, width=560, height=300)
text_field.place(x=20, y=250)

window.mainloop()