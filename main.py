




import tkinter as tk

import sqlite3




class AddressBookApp:

 def __init__(self, master):

  self.master = master

  self.master.title("Address Book")

 

  # Create a frame for the input fields

  self.input_frame = tk.Frame(self.master)

  self.input_frame.pack()

 

  # Create labels and input fields for name, address, phone, and email

  tk.Label(self.input_frame, text="Name:").grid(row=0, column=0)

  self.name_entry = tk.Entry(self.input_frame)

  self.name_entry.grid(row=0, column=1)

 

  tk.Label(self.input_frame, text="Address:").grid(row=1, column=0)

  self.address_entry = tk.Entry(self.input_frame)

  self.address_entry.grid(row=1, column=1)

 

  tk.Label(self.input_frame, text="Phone:").grid(row=2, column=0)

  self.phone_entry = tk.Entry(self.input_frame)

  self.phone_entry.grid(row=2, column=1)

 

  tk.Label(self.input_frame, text="Email:").grid(row=3, column=0)

  self.email_entry = tk.Entry(self.input_frame)

  self.email_entry.grid(row=3, column=1)

 

  # Create buttons for adding, updating, and deleting contacts

  self.button_frame = tk.Frame(self.master)

  self.button_frame.pack()

 

  tk.Button(self.button_frame, text="Add", command=self.add_contact).pack(side=tk.LEFT)

  tk.Button(self.button_frame, text="Update", command=self.update_contact).pack(side=tk.LEFT)

  tk.Button(self.button_frame, text="Delete", command=self.delete_contact).pack(side=tk.LEFT)

  tk.Button(self.button_frame, text="select", command=self.clicked).pack(side=tk.LEFT)

 

  # Create a listbox for displaying contacts

  self.contacts_listbox = tk.Listbox(self.master, width=50)

  self.contacts_listbox.pack()

 

  # Load existing contacts from the database

  self.load_contacts()

 

 def load_contacts(self):

  # Clear the listbox before reloading contacts

  self.contacts_listbox.delete(0, tk.END)

 

  # Connect to the database and retrieve contacts

  conn = sqlite3.connect("address_book.db")

  c = conn.cursor()

  c.execute("SELECT * FROM contacts")

  contacts = c.fetchall()

  conn.close()

 

  # Add each contact to the listbox

  for contact in contacts:

   self.contacts_listbox.insert(tk.END, contact[1])

 

 def add_contact(self):

  # Retrieve data from input fields

  name = self.name_entry.get()

  address = self.address_entry.get()

  phone = self.phone_entry.get()

  email = self.email_entry.get()

 

  # Connect to the database and insert new contact

  conn = sqlite3.connect("address_book.db")

  c = conn.cursor()

  c.execute("INSERT INTO contacts (name, address, phone, email) VALUES (?, ?, ?, ?)", (name, address, phone, email))

  conn.commit()

  conn.close()

 

  # Clear input fields and reload contacts

  self.name_entry.delete(0, tk.END)

  self.address_entry.delete(0, tk.END)

  self.phone_entry.delete(0, tk.END)

  self.email_entry.delete(0, tk.END)

  self.load_contacts()




 def clicked(self):

  selection = self.contacts_listbox.curselection()

  if len(selection) == 0:

   return

  contact_name =selection[0]+1
  print(selection)

  conn = sqlite3.connect("address_book.db")

  c = conn.cursor()

  c.execute(f"SELECT * FROM contacts where id={selection[0]+1}")

  contacts_detail = c.fetchall()

  conn.commit()

  conn.close()




  print(contacts_detail)

  self.name_entry.insert(0,contacts_detail[0][1])

  self.address_entry.insert(0,contacts_detail[0][2])

  self.phone_entry.insert(0,contacts_detail[0][3])

  self.email_entry.insert(0,contacts_detail[0][4])








 def update_contact(self):

  # Retrieve selected contact from the listbox

 




  # Retrieve data from

 

    # Retrieve updated data from input fields

  name = self.name_entry.get()

  address = self.address_entry.get()

  phone = self.phone_entry.get()

  email = self.email_entry.get()

 




 

  # Connect to the database and update the contact

  conn = sqlite3.connect("address_book.db")

  c = conn.cursor()

  c.execute("UPDATE contacts SET name=?, address=?, phone=?, email=? WHERE name=?", (name, address, phone, email,name))

  conn.commit()

  conn.close()

 

  # Clear input fields and reload contacts

  self.name_entry.delete(0, tk.END)

  self.address_entry.delete(0, tk.END)

  self.phone_entry.delete(0, tk.END)

  self.email_entry.delete(0, tk.END)

  self.load_contacts()

 

 def delete_contact(self):

  # Retrieve selected contact from the listbox

  selection = self.contacts_listbox.curselection()

  if len(selection) == 0:

   return

  contact_name = self.contacts_listbox.get(selection[0])

 

  # Connect to the database and delete the contact

  conn = sqlite3.connect("address_book.db")

  c = conn.cursor()

  c.execute("DELETE FROM contacts WHERE name=?", (contact_name,))

  conn.commit()

  conn.close()

 

  # Clear input fields and reload contacts

  self.name_entry.delete(0, tk.END)

  self.address_entry.delete(0, tk.END)

  self.phone_entry.delete(0, tk.END)

  self.email_entry.delete(0, tk.END)

  self.load_contacts()

 

# Create a new database if it doesn't exist

conn = sqlite3.connect("address_book.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone TEXT, email TEXT)")

conn.commit()

conn.close()




# Create the application window

root = tk.Tk()

app = AddressBookApp(root)

root.mainloop()





