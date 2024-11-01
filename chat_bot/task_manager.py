class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added."

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' removed."
        return f"Task '{task}' not found."

    def view_tasks(self):
        if not self.tasks:
            return "No tasks in your list."
        return "Your tasks:\n" + "\n".join(self.tasks)
