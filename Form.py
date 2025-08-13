import tkinter as tk

def submit():
    print("Name:", name_entry.get())
    print("Address:", address_entry.get())
    print("City:", city_entry.get())
    print("State:", state_entry.get())
    print("Zip:", zip_entry.get())
    root.destroy()  # Close window after submit

# Create main window
root = tk.Tk()
root.title("User Information Form")

# Labels and Entry fields
tk.Label(root, text="Name").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Address").grid(row=1, column=0, sticky="e")
address_entry = tk.Entry(root)
address_entry.grid(row=1, column=1)

tk.Label(root, text="City").grid(row=2, column=0, sticky="e")
city_entry = tk.Entry(root)
city_entry.grid(row=2, column=1)

tk.Label(root, text="State").grid(row=3, column=0, sticky="e")
state_entry = tk.Entry(root)
state_entry.grid(row=3, column=1)

tk.Label(root, text="Zip").grid(row=4, column=0, sticky="e")
zip_entry = tk.Entry(root)
zip_entry.grid(row=4, column=1)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=5, columnspan=2)

root.mainloop()
