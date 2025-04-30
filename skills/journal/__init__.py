import os
from datetime import datetime
from textblob import TextBlob

class JournalSkill:
    def __init__(self):
        self.base_log_path = os.path.join(os.path.dirname(__file__), "..", "..", "journal_logs")

    def summarize_entry(self, content: str) -> str:
        blob = TextBlob(content)
        sentences = blob.sentences
        if len(sentences) <= 2:
            return content
        else:
            return " ".join(str(s) for s in sentences[:2]) + "..."

    def detect_mood(self, content: str) -> str:
        polarity = TextBlob(content).sentiment.polarity
        if polarity > 0.2:
            return "Positive"
        elif polarity < -0.2:
            return "Negative"
        else:
            return "Neutral"

    def save_journal_entry(self, user: str, date: str, content: str) -> str:
        # Clean strings
        safe_user = user.replace(" ", "_").lower()
        safe_date = date.replace("/", "-").replace(" ", "_")
        
        # Create folder
        user_folder = os.path.join(self.base_log_path, safe_user)
        os.makedirs(user_folder, exist_ok=True)

        # Build file path
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_date}_{timestamp}.txt"
        file_path = os.path.join(user_folder, filename)

        # Generate summary and mood
        summary = self.summarize_entry(content)
        mood = self.detect_mood(content)

        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"User: {user}\n")
            f.write(f"Date: {date}\n")
            f.write(f"Mood: {mood}\n\n")
            f.write(f"Summary:\n{summary}\n\n")
            f.write(f"Full Entry:\n{content}\n")

        return f"Journal entry saved successfully!\nMood: {mood}\nSummary: {summary}"
