from tkinter import *
import re
import pandas as pd
import numpy as np
import customtkinter

def test(event):
    get = value.get()
    get = filter_text(get)
    output.set(df.loc[get])

def filter_text(text):
    text = text.lower()
    text = text.strip()
    pattern = r"[^\w\s]"
    text = re.sub(pattern, "",text)
    return text

df = pd.read_csv('list.csv')
df.index = df['Slang']
df = df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Slang'], axis=1)

app = customtkinter.CTk()
app.geometry("500x500")
app.title("sigma")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

value = StringVar()
output = StringVar()

l = customtkinter.CTkLabel(master=app, textvariable = output, width=140, height=30, text= "...", text_color="grey",)
e = customtkinter.CTkEntry(master=app, width=140, height=30, textvariable=value)
button = customtkinter.CTkButton(master=app, text="Перевести")

button.bind('<Button-1>', test)


e.pack(pady=10)
button.pack(pady=10)
l.pack(pady=10)

app.mainloop()
