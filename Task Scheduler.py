import json
from datetime import datetime, timedelta
import time

class TaskScheduler:
    def __init__(self, filename='tasks.json'):
        """Initialize the Task Scheduler with a specified filename for task storage."""
        self.filename = filename
        self.tasks = self.load_tasks()  # Load existing tasks from file

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)  # Return tasks as a list
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist

    def save_tasks(self):
        """Save the current tasks to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)  # Write tasks to file in JSON format

    def add_task(self, task, deadline):
        """
        Add a new task with a deadline.

        Args:
            task (str): The task description.
            deadline (str): The deadline in 'YYYY-MM-DD HH:MM' format.
        """
        self.tasks.append({'task': task, 'deadline': deadline})  # Append new task to the list
        self.save_tasks()  # Save tasks to file
        print(f"Task '{task}' added with deadline {deadline}.")

    