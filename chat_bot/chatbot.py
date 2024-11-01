import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime
import time
from threading import Thread
from patterns_responses import pairs
from weather import get_weather
from user_profiles import UserProfileManager
from task_manager import TaskManager
from reminder_manager import ReminderManager
from math_solver import solve_math_expression

# Create the chatbot
chatbot = Chat(pairs, reflections)
user_profile_manager = UserProfileManager()
task_manager = TaskManager()
reminder_manager = ReminderManager()

def handle_weather_query(user_input):
    weather_patterns = [r"how (.*) weather", r"what is the weather"]
    for pattern in weather_patterns:
        match = nltk.re.match(pattern, user_input)
        if match:
            return "Please specify the city to get the weather."
    return None

def handle_task_manager_query(user_input):
    if "add task" in user_input:
        task = input("Please specify the task to add: ")
        return task_manager.add_task(task)
    elif "remove task" in user_input:
        task = input("Please specify the task to remove: ")
        return task_manager.remove_task(task)
    elif "view tasks" in user_input or "view task" in user_input:
        return task_manager.view_tasks()
    return None

def handle_reminder_query(user_input):
    if "set reminder" in user_input:
        reminder = input("What would you like to be reminded about? ")
        time = input("When would you like to be reminded? (format: YYYY-MM-DD HH:MM:SS) ")
        time_obj = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        return reminder_manager.set_reminder(reminder, time_obj)
    elif "view reminders" in user_input:
        return reminder_manager.view_reminders()
    return None

def handle_math_query(user_input):
    if "solve" in user_input:
        expression = input("Please specify the math expression to solve: ")
        return solve_math_expression(expression)
    return None

def get_emotional_response(user_input, emotion):
    if emotion == "happy":
        return "I'm glad to hear that!"
    elif emotion == "sad":
        return "I'm sorry to hear that. I'm here for you."
    else:
        return chatbot.respond(user_input)

def provide_instructions():
    instructions = (
        "Here are some things you can ask me to do:\n"
        "- To add a task: type 'add task' and specify the task when prompted.\n"
        "- To remove a task: type 'remove task' and specify the task when prompted.\n"
        "- To view your tasks: type 'view tasks'.\n"
        "- To set a reminder: type 'set reminder' and specify the details when prompted.\n"
        "- To view your reminders: type 'view reminders'.\n"
        "- To check the weather: ask 'how is the weather' and specify the city when prompted.\n"
        "- To solve a math problem: type 'solve' and specify the math expression when prompted."
    )
    return instructions

def check_reminders():
    while True:
        current_time = datetime.now()
        due_reminders = reminder_manager.check_reminders(current_time)
        for reminder in due_reminders:
            print(f"Reminder: {reminder}")
        time.sleep(60)

# Start a separate thread to check reminders
reminder_thread = Thread(target=check_reminders, daemon=True)
reminder_thread.start()

print("Hi, I am your enhanced chatbot. Type 'quit' to exit.")
name = input("What's your name? ")
profile = user_profile_manager.get_or_create_profile(name)
print(profile.get_greeting())

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    profile.add_conversation(f"You: {user_input}")
    profile.analyze_emotion(user_input)
    emotion = profile.emotion

    if user_input.lower() == "help":
        instructions_response = provide_instructions()
        print(f"Bot: {instructions_response}")
        profile.add_conversation(f"Bot: {instructions_response}")
        continue

    reminder_response = handle_reminder_query(user_input)
    if reminder_response:
        print(f"Bot: {reminder_response}")
        profile.add_conversation(f"Bot: {reminder_response}")
        continue

    weather_response = handle_weather_query(user_input)
    if weather_response:
        print(f"Bot: {weather_response}")
        city = input("Please specify the city: ")
        weather_response = get_weather(city)
        print(f"Bot: {weather_response}")
        profile.add_conversation(f"Bot: {weather_response}")
        continue

    task_manager_response = handle_task_manager_query(user_input)
    if task_manager_response:
        print(f"Bot: {task_manager_response}")
        profile.add_conversation(f"Bot: {task_manager_response}")
        continue

    math_response = handle_math_query(user_input)
    if math_response:
        print(f"Bot: {math_response}")
        profile.add_conversation(f"Bot: {math_response}")
        continue

    response = get_emotional_response(user_input, emotion)
    print(f"Bot: {response}")
    profile.add_conversation(f"Bot: {response}")
