from tkinter import *
import re
import pandas as pd
import numpy as np

df = pd.read_csv('list.csv')
df.index = df['Slang']
df = df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Slang'], axis = 1)



root = Tk()
root.geometry("1000x1000")
root.title('Переводчик молодёжного сленга')

value = StringVar()
Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}

l = Label(text='...')
e = Entry(textvariable=value, width=45)
b = Button(text='Перевести')

def test(event):
    get = value.get()
    l["text"] = df.loc[get]

def filter_text(text):
    text = text.lower()
    text = text.strip()
    pattern = r"[^\w\s]"
    text = re.sub(pattern, "",text)
    return text
    LabelFrame = list.csv


b.bind('<Button-1>', test)
# grid  pack
e.pack()
b.pack()
l.pack()


root.mainloop()





