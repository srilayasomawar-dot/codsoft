"""
Command Line To-Do List Application

This file contains the CLI version of the project. It stores tasks in
tasks.json so that tasks remain available after the program is closed.
"""

import json
import os
from datetime import datetime


TASKS_FILE = "tasks.json"


class TaskManager:
    """Handles all task operations and file storage."""

    def __init__(self, filename=TASKS_FILE):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file when the application starts."""
        if not os.path.exists(self.filename):
            self.tasks = []
            self.save_tasks()
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except json.JSONDecodeError:
            print("Warning: tasks.json was invalid. Starting with an empty list.")
            self.tasks = []
        except OSError as error:
            print(f"Error loading tasks: {error}")
            self.tasks = []

    def save_tasks(self):
        """Save all tasks permanently in the JSON file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=4)
        except OSError as error:
            print(f"Error saving tasks: {error}")

    def add_task(self, title):
        """Add a new task."""
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")

        task = {
            "id": self.get_next_id(),
            "title": title,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        """Return all tasks."""
        return self.tasks

    def update_task(self, task_id, new_title):
        """Update the title of an existing task."""
        new_title = new_title.strip()
        if not new_title:
            raise ValueError("New task title cannot be empty.")

        task = self.find_task(task_id)
        task["title"] = new_title
        self.save_tasks()

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        task = self.find_task(task_id)
        self.tasks.remove(task)
        self.save_tasks()

    def complete_task(self, task_id):
        """Mark a task as completed."""
        task = self.find_task(task_id)
        task["completed"] = True
        self.save_tasks()

    def find_task(self, task_id):
        """Find and return a task by ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        raise ValueError("Task not found.")

    def get_next_id(self):
        """Generate the next task ID."""
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1


def display_menu():
    """Display CLI menu options."""
    print("\n========== TO-DO LIST MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")


def display_tasks(tasks):
    """Display tasks in a beginner-friendly format."""
    if not tasks:
        print("\nNo tasks found. Add your first task!")
        return

    print("\n-------------- TASKS --------------")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. [{status}] {task["title"]}')
        print(f'   Created: {task["created_at"]}')


def get_task_id():
    """Safely read task ID from the user."""
    try:
        return int(input("Enter task ID: "))
    except ValueError as exc:
        raise ValueError("Please enter a valid numeric task ID.") from exc


def main():
    """Run the CLI application."""
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                title = input("Enter task title: ")
                manager.add_task(title)
                print("Task added successfully.")

            elif choice == "2":
                display_tasks(manager.view_tasks())

            elif choice == "3":
                display_tasks(manager.view_tasks())
                task_id = get_task_id()
                new_title = input("Enter new task title: ")
                manager.update_task(task_id, new_title)
                print("Task updated successfully.")

            elif choice == "4":
                display_tasks(manager.view_tasks())
                task_id = get_task_id()
                manager.delete_task(task_id)
                print("Task deleted successfully.")

            elif choice == "5":
                display_tasks(manager.view_tasks())
                task_id = get_task_id()
                manager.complete_task(task_id)
                print("Task marked as completed.")

            elif choice == "6":
                print("Thank you for using the To-Do List Application!")
                break

            else:
                print("Invalid choice. Please choose a number from 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
