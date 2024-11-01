import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class UserProfile:
    def __init__(self, name):
        self.name = name
        self.preferences = {}
        self.conversations = []
        self.emotion = "neutral"

    def add_conversation(self, message):
        self.conversations.append(message)

    def analyze_emotion(self, message):
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(message)
        if sentiment["compound"] >= 0.5:
            self.emotion = "happy"
        elif sentiment["compound"] <= -0.5:
            self.emotion = "sad"
        else:
            self.emotion = "neutral"

    def get_greeting(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return f"Good morning, {self.name}!"
        elif current_hour < 18:
            return f"Good afternoon, {self.name}!"
        else:
            return f"Good evening, {self.name}!"

class UserProfileManager:
    def __init__(self):
        self.profiles = {}

    def get_or_create_profile(self, name):
        if name not in self.profiles:
            self.profiles[name] = UserProfile(name)
        return self.profiles[name]
