import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("400x500")

title_label = ctk.CTkLabel(
    app, 
    text="Expense Tracker", 
    font=("Arial", 24, "bold")
)
title_label.pack(pady=30)

app.mainloop()