import tkinter as tk
import pyttsx3
import threading
import random
import time
import os
from playsound import playsound

# Text-to-speech engine
voice = pyttsx3.init()
voice.setProperty('rate', 150)

# Funny troll phrases
phrases = [
    "Hey! Did you do your homework?",
    "ZéManéBuddy is watching you!",
    "Go study instead of playing with me!",
    "Your mom knows you're running this?",
    "Totally NOT a virus... or is it?",
    "Nicolas has summoned me 😈",
]

# Path to Rickroll music file
rickroll_path = "rick.mp3"

# Speak random phrases
def talk():
    while True:
        time.sleep(random.randint(10, 20))
        phrase = random.choice(phrases)
        voice.say(phrase)
        voice.runAndWait()

# Play Rickroll
def play_rickroll():
    time.sleep(random.randint(15, 25))
    playsound(rickroll_path)

# Open troll windows
def open_windows():
    for _ in range(10):
        x = random.randint(100, 800)
        y = random.randint(100, 500)
        t = threading.Thread(target=show_window, args=(x, y))
        t.start()
        time.sleep(random.uniform(1, 2))

# Troll window function
def show_window(x, y):
    win = tk.Tk()
    win.title("ZéManéBuddy 😂")
    win.geometry(f"250x200+{x}+{y}")
    win.configure(bg="purple")

    label = tk.Label(win, text="🦍", font=("Arial", 80), bg="purple")
    label.pack()

    button = tk.Button(win, text="Close me if you can!", command=win.destroy)
    button.pack()

    win.mainloop()

# Launch everything
threading.Thread(target=talk).start()
threading.Thread(target=play_rickroll).start()
threading.Thread(target=open_windows).start()
