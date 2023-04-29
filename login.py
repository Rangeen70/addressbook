import tkinter as tk
import sqlite3

def login_user():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    if user:
        if user[1] == password:
            conn.close()
            root.destroy()
            import main
        else:
            error_label.config(text="Incorrect password")
    else:
        error_label.config(text="Incorrect username")

root = tk.Tk()
root.title("Login Page")
root.geometry("300x150")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login_user)
login_button.pack()

error_label = tk.Label(root, fg="red")
error_label.pack()

root.mainloop()
