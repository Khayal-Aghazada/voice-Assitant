import speech_recognition as sr
import pyttsx3
import pyautogui
import webbrowser
import os
import time
import datetime
import psutil 
from googletrans import Translator


# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 190)  # Faster speech

translator = Translator()  # Google Translator

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for a voice command with minimal delay."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening...")
        
        try:
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)  # Faster listening
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Didn't catch that.")
            return ""
        except sr.RequestError:
            print("Could not connect to Google Speech API.")
            return ""
        except sr.WaitTimeoutError:
            print("Timeout, waiting for next command...")
            return ""

def switch_to_browser():
    """Brings the browser window to the front (YouTube must be open)."""
    speak("Switching to browser")
    pyautogui.hotkey("alt", "tab")  # Press Alt + Tab to switch windows
    time.sleep(1)  # Give it a second to switch

def next_video():
    """Switches to the browser and skips to the next YouTube video."""
    switch_to_browser()
    pyautogui.hotkey("shift", "n")
    speak("Next video")

def previous_video():
    """Switches to the browser and plays the previous YouTube video."""
    switch_to_browser()
    pyautogui.hotkey("shift", "p")
    speak("Previous video")

def next_tab():
    """Switches to the next browser tab."""
    speak("Switching to next tab")
    pyautogui.hotkey("alt", "tab")

def previous_tab():
    """Switches to the previous browser tab."""
    speak("Switching to previous tab")
    pyautogui.hotkey("ctrl", "shift", "tab")

def close_application(app_name):
    """Closes an application by its process name."""
    speak(f"Closing {app_name}")
    os.system(f"taskkill /f /im {app_name}")

def open_application(app_name, paths):
    """Tries to open an application from a list of possible paths."""
    for path in paths:
        if os.path.exists(path):
            speak(f"Opening {app_name}")
            os.startfile(path)
            return
    speak(f"Could not find {app_name}. Make sure it's installed.")

def take_screenshot():
    """Takes a screenshot and saves it as screenshot.png."""
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot saved.")

def close_specific_app(app_name):
    """Closes a specific application by name."""
    found = False
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if app_name.lower() in process.info['name'].lower():
                os.system(f"taskkill /f /pid {process.info['pid']}")  # Force close the app
                speak(f"{app_name} has been closed.")
                found = True
        except Exception as e:
            print(f"Could not close {app_name}: {e}")

    if not found:
        speak(f"{app_name} is not open.")

def close_specific_app(app_name):
    """Closes a specific application by name."""
    found = False
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if app_name.lower() in process.info['name'].lower():
                os.system(f"taskkill /f /pid {process.info['pid']}")  # Force close the app
                speak(f"{app_name} has been closed.")
                found = True
        except Exception as e:
            print(f"Could not close {app_name}: {e}")

    if not found:
        speak(f"{app_name} is not open.")

def minimize_window():
    """Minimizes the current active window."""
    speak("Minimizing window.")
    pyautogui.hotkey("win", "down")  # Minimize window

def maximize_window():
    """Maximizes the current active window."""
    speak("Maximizing window.")
    pyautogui.hotkey("win", "up")  # Maximize window

def execute_command(command):
    """Executes the voice command quickly."""
    
    commands = {
        # Applications
        "chrome": lambda: os.system("start chrome"),
        "notepad": lambda: os.system("notepad"),
        "vs code": lambda: os.system("code"),  
        "word": lambda: os.system("start winword"),  
        "excel": lambda: os.system("start excel"),  
        "powerpoint": lambda: os.system("start powerpnt"),  

        # WhatsApp, Telegram, Discord, Outlook
        "vp": lambda: open_application("WhatsApp", [
            r"C:WhatsApp.exe",
        ]),

        "telegram": lambda: open_application("Telegram", [
            r"C:\Users\aghaz\AppData\Roaming\Telegram Desktop\Telegram.exe",
        ]),
        "outlook": lambda: os.system("start outlook"),  

        "discord": lambda: open_application("Discord", [
            r"C:Discord.exe",
        ]),

        # Close Applications
        "close vsp": lambda: close_application("WhatsApp.exe"),
        "close tg": lambda: close_application("Telegram.exe"),
        "close dc": lambda: close_application("Discord.exe"),
        "close ot": lambda: close_application("OUTLOOK.EXE"),
        "close c": lambda: close_application("chrome.exe"),

        # System Controls
        "mute": lambda: pyautogui.press("volumemute"),
        "louder": lambda: pyautogui.press("volumeup", presses=5),
        "quieter": lambda: pyautogui.press("volumedown", presses=5),

        "minimize window": lambda: minimize_window(),
        "maximize window": lambda: maximize_window(),

        # File Management
        "create file": lambda: open("new_file.txt", "w").close(),
        "delete file": lambda: os.remove("new_file.txt") if os.path.exists("new_file.txt") else speak("File not found"),
        "screenshot": lambda: take_screenshot(),

        # Time & Date
        "time": lambda: speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}"),
        "date": lambda: speak(f"Today's date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}"),

        # Browser Actions (Fixed Next/Previous Video)
        "pause": lambda: pyautogui.press("k"),
        "play": lambda: pyautogui.press("k"),
        "next video": lambda: next_video(),

        # New Tab Switching Commands
        "next window": lambda: next_tab(),
        "previous window": lambda: previous_tab(),
        "close everything": lambda: close_everything(),
         
        # System Shutdown
        "shut down": lambda: os.system("shutdown /s /t 5"),
        "restart": lambda: os.system("shutdown /r /t 5"),
        "lock": lambda: os.system("rundll32.exe user32.dll,LockWorkStation"),

        "exit": lambda: exit_program()
    }
    
    if "translate" in command:
        word_to_translate = command.replace("translate ", "")
        speak(f"Translating {word_to_translate}")
        translated = translator.translate(word_to_translate, dest="ru").text
        print(f"Translation: {translated}")
        speak(translated)
        return

    if "search for" in command:
        search_query = command.replace("search for ", "")
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        return

    for key, action in commands.items():
        if key in command:
            speak(f"Executing {key}")
            action()
            return

    speak("I didn't understand that command.")


    if command.startswith("close "):
        app_name = command.replace("close ", "").strip()
        close_specific_app(app_name)
        return

    for key, action in commands.items():
        if key in command:
            speak(f"Executing {key}")
            action()
            return

    speak("I didn't understand that command.")

def exit_program():
    """Exits the assistant."""
    speak("Goodbye!")
    exit(0)

# Main loop with minimal delay
speak("Voice Assistant is ready!")
while True:
    try:
        user_command = listen()
        if user_command:
            execute_command(user_command)
    except Exception as e:
        print(f"Error: {e}. Restarting listening...")
