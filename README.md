# To-Do List Application

A beginner-friendly Python mini project that helps users create, view, edit, delete, complete, and permanently save daily tasks. The project includes both a Command Line Interface version and a Tkinter GUI version.

## Project Structure

```text
To-Do-List-Application/
├── main.py
├── gui.py
├── tasks.json
└── README.md
```

## Features

- Add new tasks
- View all saved tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Store tasks permanently in `tasks.json`
- Load saved tasks automatically when the application starts
- CLI version for terminal users
- GUI version with Tkinter buttons, input field, list display, colors, and fonts
- Error handling for empty input, invalid task IDs, missing files, and invalid JSON

## Technologies Used

- Python 3
- Tkinter for GUI
- JSON for file storage
- Standard Python libraries: `json`, `os`, `datetime`, `tkinter`

## Requirements

No external packages are required.

You only need Python 3 installed. Tkinter is included with most standard Python installations.

## Installation Instructions

1. Install Python 3 from <https://www.python.org/downloads/>.
2. Download or clone this project folder.
3. Open a terminal or command prompt in the project directory.
4. Run the CLI version:

```bash
python main.py
```

5. Run the GUI version:

```bash
python gui.py
```

## How To Use CLI Version

1. Start the program using `python main.py`.
2. Choose an option from the menu.
3. Add, view, update, delete, or complete tasks.
4. Choose option `6` to exit.

### Sample CLI Output

```text
========== TO-DO LIST MENU ==========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task as Completed
6. Exit
Enter your choice (1-6): 1
Enter task title: Complete Python assignment
Task added successfully.
```

## How To Use GUI Version

1. Start the program using `python gui.py`.
2. Type a task in the input field.
3. Click `Add Task`.
4. Select a task from the list.
5. Use `Edit Task`, `Complete Task`, or `Delete Task`.

## Sample Output Screenshots Description

### CLI Screenshot Description

The terminal displays a menu with six options. After adding a task, a success message appears. When viewing tasks, each task is shown with its task ID, completion status, title, and creation date.

### GUI Screenshot Description

The GUI window has a light background, a bold title at the top, an input field with an `Add Task` button, a large task list area, and three action buttons: `Edit Task`, `Complete Task`, and `Delete Task`. Completed tasks appear in a muted color.

## Step-By-Step Explanation

### 1. Task Storage

Tasks are stored in `tasks.json`. Each task contains:

- `id`: unique task number
- `title`: task text
- `completed`: task status
- `created_at`: date and time when the task was created

Example:

```json
{
    "id": 1,
    "title": "Study Python",
    "completed": false,
    "created_at": "2026-05-22 10:30:00"
}
```

### 2. TaskManager Class

Both `main.py` and `gui.py` contain a `TaskManager` class. This class handles:

- Loading tasks from JSON
- Saving tasks to JSON
- Adding tasks
- Updating tasks
- Deleting tasks
- Marking tasks as completed
- Finding tasks by ID

### 3. CLI Application

The CLI version uses a loop to display a menu. The user enters a number from 1 to 6. Based on the choice, the program calls the correct function.

### 4. GUI Application

The GUI version uses Tkinter widgets:

- `Entry` for task input
- `Button` for actions
- `Listbox` for task display
- `Scrollbar` for scrolling
- `messagebox` for alerts
- `simpledialog` for editing tasks

### 5. File Handling

When the app starts, it loads tasks from `tasks.json`. After every add, edit, delete, or complete action, the program saves the latest task list back to the file.

## Mini Project Report

### Introduction

The To-Do List Application is a Python-based mini project designed to help users manage daily tasks. It provides an easy way to add, view, update, delete, and complete tasks. The project includes both a command-line interface and a graphical user interface.

### Objective

The objective of this project is to create a simple and useful task management application while learning Python programming concepts such as classes, functions, file handling, exception handling, and GUI development.

### Features

- User can add new tasks.
- User can view all tasks.
- User can update existing tasks.
- User can delete unwanted tasks.
- User can mark tasks as completed.
- Tasks are saved permanently using JSON file handling.
- Application is available in both CLI and GUI formats.

### Technologies Used

- Python 3 for programming logic
- Tkinter for the graphical interface
- JSON file for permanent data storage
- Visual Studio Code or any Python IDE for development

### Advantages

- Easy to use and beginner-friendly
- Does not require internet access
- No external packages required
- Stores data permanently
- Helps users organize daily work
- Demonstrates important Python concepts clearly

### Future Enhancements

- Add task due dates
- Add task priority levels
- Add search and filter options
- Add categories for tasks
- Add notifications or reminders
- Use SQLite database instead of JSON
- Add user login system

### Conclusion

The To-Do List Application successfully demonstrates how Python can be used to build practical software. It covers important concepts such as object-oriented programming, file handling, error handling, and GUI design. This project is useful for beginners and can be extended with more advanced features in the future.

## Resume Project Description

**To-Do List Application using Python**

Developed a Python-based To-Do List Application with both CLI and Tkinter GUI interfaces. Implemented task creation, viewing, editing, deletion, completion tracking, and permanent JSON file storage. Used object-oriented programming, file handling, exception handling, and a clean user interface to build a beginner-friendly productivity tool.

## GitHub README Content

You can use this same `README.md` file as your GitHub README. It already includes project overview, features, installation steps, usage instructions, sample output, explanation, project report, viva questions, and interview questions.

## Viva Questions And Answers

### 1. What is the purpose of this project?

The purpose of this project is to manage daily tasks using a Python application that supports adding, viewing, editing, deleting, and completing tasks.

### 2. Which programming language is used?

Python is used to build this project.

### 3. What is Tkinter?

Tkinter is Python's standard library for creating graphical user interfaces.

### 4. Why is JSON used in this project?

JSON is used because it is simple, readable, and suitable for storing structured task data permanently.

### 5. What is file handling?

File handling is the process of reading data from files and writing data to files.

### 6. What is a class?

A class is a blueprint for creating objects. In this project, `TaskManager` is a class that manages task operations.

### 7. What is exception handling?

Exception handling is used to handle errors during program execution without crashing the application.

### 8. How are tasks saved permanently?

Tasks are saved permanently by writing them to the `tasks.json` file after every change.

### 9. How does the program identify each task?

Each task has a unique numeric `id`.

### 10. Can this project be improved?

Yes. It can be improved by adding due dates, priorities, reminders, categories, search, and database support.

## Interview Questions Related To The Project

### 1. Explain the architecture of your To-Do List Application.

The project has two interfaces: CLI and GUI. Both use a `TaskManager` class for core task operations and JSON file handling. The CLI uses terminal input and output, while the GUI uses Tkinter widgets.

### 2. Why did you choose JSON instead of a database?

JSON is simple, easy to understand, and enough for a beginner-level project. It avoids database setup while still providing permanent storage.

### 3. How did you implement task completion?

Each task has a Boolean field named `completed`. When the user marks a task as complete, this value changes from `false` to `true`.

### 4. How does your application handle errors?

The application uses `try-except` blocks to handle invalid task IDs, empty input, missing files, invalid JSON, and file read/write errors.

### 5. What object-oriented concepts are used?

The project uses classes, objects, methods, and encapsulation. The `TaskManager` class keeps task-related logic organized in one place.

### 6. How is the GUI updated after adding or deleting a task?

The GUI calls `refresh_task_list()`, which clears the Listbox and inserts the latest tasks from memory.

### 7. What are the limitations of this project?

The project does not include due dates, reminders, user accounts, or advanced filtering. It is designed as a beginner-friendly mini project.

### 8. How would you scale this project?

I would move storage from JSON to SQLite or PostgreSQL, add a login system, implement due dates and priorities, and create a web or mobile version.

## Author

Created as a Python mini project for learning and demonstration purposes.
