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

    def check_reminders(self):
        """Check for tasks that are due within the next hour."""
        current_time = datetime.now()
        upcoming_tasks = []


        for task in self.tasks:
            task_deadline = datetime.strptime(task['deadline'], '%Y-%m-%d %H:%M')
            if current_time <= task_deadline < current_time + timedelta(hours=1):
                upcoming_tasks.append(task)  # Collect tasks due in the next hour


        return upcoming_tasks  # Return the list of upcoming tasks


def main():
    """Main function to run the Task Scheduler."""
    scheduler = TaskScheduler()  # Create an instance of TaskScheduler

    while True:
        print("\nTask Scheduler")
        print("1. Add Task")
        print("2. Check Reminders")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            deadline_input = input("Enter deadline (YYYY-MM-DD HH:MM): ")
            try:
                # Validate the deadline format
                datetime.strptime(deadline_input, '%Y-%m-%d %H:%M')
                scheduler.add_task(task_description, deadline_input)  # Add the task
            except ValueError:
                print("Invalid date format. Please use 'YYYY-MM-DD HH:MM'.")


        elif choice == '2':
            reminders = scheduler.check_reminders()  # Check for upcoming tasks
            if reminders:
                print("Upcoming tasks:")
                for reminder in reminders:
                    print(f"- {reminder['task']} (Deadline: {reminder['deadline']})")
            else:
                print("No upcoming tasks within the next hour.")


        elif choice == '3':
            print("Exiting Task Scheduler. Goodbye!")
            break  # Exit the loop


        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()  #
