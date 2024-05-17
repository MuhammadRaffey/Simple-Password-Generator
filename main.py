import tkinter as tk
from tkinter.constants import END
import random

class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Random Password Generator")
        self.configure(bg="#00FFFF")
        self.iconbitmap('background.ico')

        self.create_widgets()

    def create_widgets(self):
        self.label_instruction = tk.Label(self, text="Enter name of your account", bg="#FF002B", fg="#FFFB00")
        self.label_instruction.place(x=190, y=55)

        self.entry_account = tk.Entry(self, width=50, background="yellow")
        self.entry_account.place(x=140, y=80)
        self.entry_account.insert(0, "enter your gmail")

        if "enter your gmail" in self.entry_account.get():
            self.after(2000, self.remove_placeholder)

        self.button_enter = tk.Button(self, text="Enter", command=self.display_account, bg="#FF002B", fg="#FFFB00")
        self.button_enter.place(x=250, y=100)

        self.button_generate_password = tk.Button(self, text="Generate password", command=self.generate_password, bg="#FF002B", fg="#FFFB00")
        self.button_generate_password.place(x=200, y=155)

        self.button_refresh = tk.Button(self, text="Refresh", command=self.refresh, bg="#FF002B", fg="#FFFB00")
        self.button_refresh.place(x=230, y=215)

        self.button_exit = tk.Button(self, text="Exit", command=self.quit, bg='#FF002B', fg='#FFFB00')
        self.button_exit.place(x=240, y=250)

    def remove_placeholder(self):
        if self.entry_account.get() == "enter your gmail":
            self.entry_account.delete(0, END)

    def display_account(self):
        account_name = self.entry_account.get()
        self.label_account = tk.Label(self, text=f"Your account name is:\t{account_name}", bg="yellow", fg="black")
        self.label_account.place(x=155, y=130)

    def generate_password(self):
        chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-=+/.,'"
        length = 20
        password = "".join(random.sample(chars, length))
        self.label_password = tk.Label(self, text=f"Your password is \t{password}", bg="yellow", fg="black")
        self.label_password.place(x=155, y=190)
        with open("Passwords.txt", 'a') as file:
            file.write(f"\n{self.entry_account.get()}:\t{password}")

    def refresh(self):
        self.entry_account.delete(0, END)
        if hasattr(self, 'label_account'):
            self.label_account.destroy()
        if hasattr(self, 'label_password'):
            self.label_password.destroy()

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
