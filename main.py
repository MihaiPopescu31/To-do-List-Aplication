import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    # Function to add a task to the list and save it to the file
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks_to_file()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    # Function to delete a task from the list and update the file
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks_to_file()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def complete_task():
    # Function to mark the selected task as completed
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, bg="light green")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete!")

def save_tasks_to_file():
    # Function to save tasks to the tasks.txt file
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Creating the main window
root = tk.Tk()
root.title("Todo List")
root.geometry("400x300")

# Style for buttons
new_style = ttk.Style()
new_style.configure("New.TButton", foreground="white", background="#FF5733", font=('Helvetica', 12))

# Label and entry for adding tasks
tk.Label(root, text="Task:", font=("Helvetica", 12)).pack(anchor="w", padx=10, pady=(10, 0))
task_entry = tk.Entry(root, font=("Helvetica", 12))
task_entry.pack(anchor="w", padx=10)

# Button to add tasks
add_button = ttk.Button(root, text="Add Task", style="New.TButton", command=add_task)
add_button.pack(anchor="w", padx=10, pady=(5, 0))

# Listbox to display tasks
task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=50, height=10)
task_listbox.pack(anchor="w", padx=10, pady=5)

# Buttons to delete and mark tasks as completed
delete_button = ttk.Button(root, text="❌", style="New.TButton", command=delete_task)
delete_button.pack(side="left", padx=10, pady=5)

complete_button = ttk.Button(root, text="✅", style="New.TButton", command=complete_task)
complete_button.pack(side="left", padx=10, pady=5)

root.mainloop()
