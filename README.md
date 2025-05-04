ASA Pro – AI Semantic Agent

ASA Pro is a voice-enabled journaling assistant built with Python.It allows users to:

✍️ Record timestamped journal entries

🧠 Automatically summarize logs using NLP (TextBlob)

🌭 Detect sentiment (positive, negative, neutral)

🎤 Use voice commands to search journal entries

🔊 Hear ASA read entries aloud using text-to-speech

📁 Project Structure

ASA_Pro_Project/
├── astra_agent.py          # Kernel and skill loader  
├── main_sk.py              # Logs a new journal entry  
├── voice_search.py         # Voice search + TTS output  
├── semantic_kernel/        # Local skill/kernel framework  
├── skills/
│   └── journal/
│       └── __init__.py     # JournalSkill (summary + mood)
├── journal_logs/           # Saved logs by user  
├── requirements.txt        # Dependencies for venv  
└── venv/                   # Virtual environment (optional to zip)  

🚀 How to Run

🧚i Record a Journal Entry

python main_sk.py

🎤 Search Your Journals by Voice

python voice_search.py

Say things like:

"Show positive entries"

"Find logs from April"

"Search ASA launch"

ASA will print + speak matching summaries.

💾 Setup Instructions

1. Create and Activate Virtual Environment

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

2. Install Dependencies

pip install -r requirements.txt
python -m textblob.download_corpora

✅ Requirements (Included in requirements.txt)

pyttsx3

SpeechRecognition

textblob

nltk

PyAudio

pypiwin32 (Windows only)

🤖 Optional: Raspberry Pi Deployment

ASA runs fully offline on Raspberry Pi with USB mic + speaker.

Headless mode coming soon

Great for journaling in remote environments or travel

🧠 Author  
Created by Natalia Solorzano  
Capstone Project – AI Agent Prototype  
April 2025  

📌 License  
Copyright © 2025 Natalia Solorzano  
All content, code, and visual assets in this repository are original works.  
Use or reproduction without explicit permission is strictly prohibited.



