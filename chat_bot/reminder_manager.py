import datetime

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, reminder, time):
        self.reminders.append((reminder, time))
        return f"Reminder set for {time}: {reminder}"

    def check_reminders(self, current_time):
        due_reminders = [reminder for reminder, time in self.reminders if time <= current_time]
        self.reminders = [(reminder, time) for reminder, time in self.reminders if time > current_time]
        return due_reminders
    
    def view_reminders(self):
        if not self.reminders:
            return "No upcoming reminders."
        reminders_list = "\n".join([f"{time}: {reminder}" for reminder, time in self.reminders])
        return f"Your upcoming reminders:\n{reminders_list}"
