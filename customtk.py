import customtkinter

app = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

button = customtkinter.CTkButton(master=app, text="Перевести")
button.place(relx=0.5, rely=0.1,)

app.title("sigma")





app.mainloop()