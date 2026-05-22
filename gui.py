"""
Tkinter To-Do List Application

This file contains the GUI version of the project. It uses the same JSON
storage format as the CLI version, so both applications share the same tasks.
"""

import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, simpledialog


TASKS_FILE = "tasks.json"


class TaskManager:
    """Handles task operations and JSON file handling for the GUI."""

    def __init__(self, filename=TASKS_FILE):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks automatically from the JSON file."""
        if not os.path.exists(self.filename):
            self.tasks = []
            self.save_tasks()
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except json.JSONDecodeError:
            messagebox.showwarning(
                "File Warning",
                "tasks.json was invalid. The application will start empty.",
            )
            self.tasks = []
        except OSError as error:
            messagebox.showerror("File Error", f"Could not load tasks: {error}")
            self.tasks = []

    def save_tasks(self):
        """Save tasks permanently to the JSON file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=4)
        except OSError as error:
            messagebox.showerror("File Error", f"Could not save tasks: {error}")

    def add_task(self, title):
        """Add a new task to the list."""
        title = title.strip()
        if not title:
            raise ValueError("Please enter a task.")

        self.tasks.append(
            {
                "id": self.get_next_id(),
                "title": title,
                "completed": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self.save_tasks()

    def update_task(self, task_id, new_title):
        """Update the selected task title."""
        new_title = new_title.strip()
        if not new_title:
            raise ValueError("Task title cannot be empty.")

        task = self.find_task(task_id)
        task["title"] = new_title
        self.save_tasks()

    def delete_task(self, task_id):
        """Delete a selected task."""
        task = self.find_task(task_id)
        self.tasks.remove(task)
        self.save_tasks()

    def complete_task(self, task_id):
        """Mark a selected task as completed."""
        task = self.find_task(task_id)
        task["completed"] = True
        self.save_tasks()

    def find_task(self, task_id):
        """Find a task by ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise ValueError("Selected task was not found.")

    def get_next_id(self):
        """Generate the next available task ID."""
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1


class TodoApp:
    """Creates and controls the Tkinter user interface."""

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("650x520")
        self.root.minsize(560, 460)
        self.root.configure(bg="#edf2f7")

        self.manager = TaskManager()
        self.task_id_lookup = []

        self.create_widgets()
        self.refresh_task_list()

    def create_widgets(self):
        """Create all GUI widgets and layout."""
        title_label = tk.Label(
            self.root,
            text="To-Do List Application",
            font=("Segoe UI", 22, "bold"),
            bg="#edf2f7",
            fg="#1a202c",
        )
        title_label.pack(pady=(18, 8))

        input_frame = tk.Frame(self.root, bg="#edf2f7")
        input_frame.pack(fill="x", padx=28, pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 12),
            bg="white",
            fg="#1a202c",
            relief="solid",
            bd=1,
        )
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=8)
        self.task_entry.bind("<Return>", lambda _event: self.add_task())

        add_button = tk.Button(
            input_frame,
            text="Add Task",
            command=self.add_task,
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=16,
            pady=8,
        )
        add_button.pack(side="left", padx=(10, 0))

        list_frame = tk.Frame(self.root, bg="#edf2f7")
        list_frame.pack(fill="both", expand=True, padx=28, pady=12)

        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Segoe UI", 12),
            bg="white",
            fg="#1a202c",
            selectbackground="#bfdbfe",
            selectforeground="#111827",
            relief="solid",
            bd=1,
            activestyle="none",
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.task_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        button_frame = tk.Frame(self.root, bg="#edf2f7")
        button_frame.pack(fill="x", padx=28, pady=(4, 18))

        self.create_action_button(
            button_frame, "Edit Task", self.edit_task, "#7c3aed", "#6d28d9"
        )
        self.create_action_button(
            button_frame, "Complete Task", self.complete_task, "#059669", "#047857"
        )
        self.create_action_button(
            button_frame, "Delete Task", self.delete_task, "#dc2626", "#b91c1c"
        )

    def create_action_button(self, parent, text, command, bg_color, active_color):
        """Create a styled action button."""
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg=bg_color,
            fg="white",
            activebackground=active_color,
            activeforeground="white",
            relief="flat",
            padx=14,
            pady=9,
        )
        button.pack(side="left", expand=True, fill="x", padx=5)

    def refresh_task_list(self):
        """Refresh the listbox after any change."""
        self.task_listbox.delete(0, tk.END)
        self.task_id_lookup = []

        for task in self.manager.tasks:
            status = "Done" if task["completed"] else "Pending"
            display_text = f'{task["id"]}. [{status}] {task["title"]}'
            self.task_listbox.insert(tk.END, display_text)
            self.task_id_lookup.append(task["id"])

            if task["completed"]:
                self.task_listbox.itemconfig(tk.END, fg="#64748b")

    def get_selected_task_id(self):
        """Return the selected task ID from the listbox."""
        selected = self.task_listbox.curselection()
        if not selected:
            raise ValueError("Please select a task first.")
        return self.task_id_lookup[selected[0]]

    def add_task(self):
        """Add a task from the input field."""
        try:
            self.manager.add_task(self.task_entry.get())
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        except ValueError as error:
            messagebox.showwarning("Input Error", str(error))

    def edit_task(self):
        """Edit the selected task."""
        try:
            task_id = self.get_selected_task_id()
            task = self.manager.find_task(task_id)
            new_title = simpledialog.askstring(
                "Edit Task",
                "Enter updated task:",
                initialvalue=task["title"],
                parent=self.root,
            )

            if new_title is not None:
                self.manager.update_task(task_id, new_title)
                self.refresh_task_list()
        except ValueError as error:
            messagebox.showwarning("Selection Error", str(error))

    def complete_task(self):
        """Mark the selected task as completed."""
        try:
            task_id = self.get_selected_task_id()
            self.manager.complete_task(task_id)
            self.refresh_task_list()
        except ValueError as error:
            messagebox.showwarning("Selection Error", str(error))

    def delete_task(self):
        """Delete the selected task after confirmation."""
        try:
            task_id = self.get_selected_task_id()
            answer = messagebox.askyesno(
                "Confirm Delete", "Are you sure you want to delete this task?"
            )
            if answer:
                self.manager.delete_task(task_id)
                self.refresh_task_list()
        except ValueError as error:
            messagebox.showwarning("Selection Error", str(error))


def main():
    """Start the Tkinter application."""
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
