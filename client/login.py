import tkinter as tk
from tkinter import messagebox
from client import *
import bcrypt
from client.gui import App
import threading
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("500x200")

        # Username label and entry
        tk.Label(self, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        tk.Label(self, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        tk.Button(self, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Create User button 
        tk.Button(self, text="Create", command=self.new_user).grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Example validation logic
        if username == "admin" and password == "password":
            self.destroy()  # Close the login window

            # Launch the main application window directly
            main_app = App()
            main_app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def new_user(self):
        new_username = self.username_entry.get()
        new_password = self.password_entry.get()

        # Example logic for creating a new user
        if new_username and new_password:
            messagebox.showinfo("User Created", f"User {new_username} created successfully!")
        else:
            messagebox.showerror("Error", "Please enter a valid username and password")
            return self.new_user


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()


