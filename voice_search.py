import os
import speech_recognition as sr
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Optional: adjust speech speed
    engine.say(text)
    engine.runAndWait()


def listen_for_search_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Say your search command (e.g., 'Show positive entries', 'Find April logs')...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=6)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🧠 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Speech recognition error: {e}")
        return None

def search_journal_logs(user_folder, search_query):
    if not os.path.exists(user_folder):
        print(f"❌ No logs found for user at: {user_folder}")
        return

    found = False
    # Split search query into keywords
    important_words = search_query.replace("find", "").replace("show", "").replace("entries", "").split()
    important_words = [word.strip() for word in important_words if word.strip()]

    for filename in os.listdir(user_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(user_folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().lower()

                for keyword in important_words:
                    if keyword in content:
                        print(f"🔎 Found match for '{keyword}' in: {filename}")
                        print("-------------------------------------")
                        print(content)
                        print("-------------------------------------\n")
                        # Extract mood and summary for voice output
                        mood_line = [line for line in content.splitlines() if line.startswith("mood:")]
                        summary_index = content.find("summary:")
                        summary = content[summary_index + 8:].split("full entry:")[0].strip() if "summary:" in content else "No summary found"
                        mood = mood_line[0].split(":")[1].strip() if mood_line else "unknown"

                        # ASA speaks!
                        speak_text(f"This entry is tagged as {mood}. Summary says: {summary}")

                        found = True
                        break  # Don't show same file twice

    if not found:
        print(f"😢 No entries matched '{search_query}'.")


def main():
    # Update this to match your username folder
    username = "natalia"
    user_logs_folder = os.path.join("journal_logs", username)

    command = listen_for_search_command()
    if command:
        search_journal_logs(user_logs_folder, command)

if __name__ == "__main__":
    main()
