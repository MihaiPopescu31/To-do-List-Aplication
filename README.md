# To-Do List Application

This is a simple to-do list application built using Python and Tkinter. It allows users to add tasks, delete tasks, and mark tasks as completed.

## Features

- **Add Task**: Users can add tasks to the to-do list by entering the task in the input field and clicking the "Add Task" button.

- **Delete Task**: Users can delete tasks from the to-do list by selecting the task and clicking the delete button (❌).

- **Complete Task**: Users can mark tasks as completed by selecting the task and clicking the complete button (✅). The completed task will be highlighted with a light green background.

- **Save to File**: The application automatically saves the tasks to a file named `tasks.txt`. This file is updated whenever a task is added or deleted.
## Requirements

- Python 3.x
- Tkinter (Python GUI library)

## Code Explanation

In this section, we'll walk through the code step by step to understand how the application works.

### Function `add_task()`

This function is called when the user clicks the "Add Task" button. It retrieves the task text entered by the user from the input field and adds it to the task listbox.

### Function `delete_task()`

When the user clicks the delete button (❌), this function is triggered. It deletes the selected task from the task listbox.

### Function `complete_task()`

This function is called when the user clicks the complete button (✅). It marks the selected task as completed by changing its background color to light green.

### Creating the Main Window

The `tk.Tk()` function is used to create the main window of the application. We set the title to "Todo List" and specify the window dimensions.

### Styling the Buttons

We use the `ttk.Style()` function to define a custom style for the buttons. The style is configured to have a flat relief, white text color, and a background color of #FF5733.

### Label and Entry for Adding Tasks

A label and an entry widget are created to allow users to input tasks. The label displays "Task:", and the entry widget allows users to enter task text.

### Button for Adding Tasks

The "Add Task" button is created using the `ttk.Button()` function. It is associated with the `add_task()` function and styled using the custom style we defined earlier.

### Listbox for Displaying Tasks

A listbox widget is used to display the tasks added by the user. It has a fixed width of 50 characters and a height of 10 lines.

### Buttons for Deleting and Completing Tasks

Two buttons are created for deleting and completing tasks. The delete button (❌) is associated with the `delete_task()` function, while the complete button (✅) is associated with the `complete_task()` function.

## Usage

1. Clone the repository:https://github.com/MihaiPopescu31/To-do-List-Aplication/blob/master/portfolio.txt

2. Navigate to the project directory in your terminal or command prompt
  
3. Run the application:python main.py
   
4. The application window will open. You can now add, delete, and complete tasks using the buttons provided.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## How to tweak this project for your own uses
Since this is an example project,i'd encourage you to clone and rename this project to use for your own purpeses.

## Find a bug
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above.
