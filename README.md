# 🗣️ WhisprAI – Your Voice-Controlled Desktop Assistant

WhisprAI is a fast and flexible voice assistant for your computer, built using Python.  
It listens to your voice commands and automates desktop actions — from opening Chrome to translating words, taking screenshots, controlling media, and more.

---

## ✨ Features

- 🎙️ Voice-based interaction via Google Speech API
- 🧠 Execute custom system commands:
  - Open/close Chrome, VS Code, Notepad, Telegram, Discord
  - Take screenshots, create/delete files
  - Maximize/minimize windows
- 📺 Control YouTube:
  - Play/pause, next/previous video
- 🔍 Translate words (e.g., “translate hello” → Russian)
- 🌐 Voice web search: “search for cats”
- 📅 System info: get time/date
- 🔊 Volume & shutdown control

---

## 🛠️ Tech Stack

- **Python 3**
- `speech_recognition` — for voice input
- `pyttsx3` — for text-to-speech
- `pyautogui` — for desktop automation
- `psutil`, `os` — for process control
- `googletrans` — for translation
- `webbrowser`, `datetime`, `time`

---

## 📦 Installation

### 🔧 Dependencies

```bash
pip install speechrecognition pyttsx3 pyautogui psutil googletrans==4.0.0-rc1
