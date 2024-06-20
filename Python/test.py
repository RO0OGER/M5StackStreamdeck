import tkinter as tk
from tkinter import messagebox
import subprocess
import psutil
import time
import os
import pyautogui

class NotepadStarterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad Starter")

        # Passwort-Label und Passwort-Eingabefeld hinzufügen
        self.password_label = tk.Label(root, text="Passwort:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=10)

        # Start-Button hinzufügen
        self.start_button = tk.Button(root, text="Start Notepad", command=self.start_notepad)
        self.start_button.pack(pady=10)

    def start_notepad(self):
        entered_password = self.password_entry.get()
        if entered_password == "dein_passwort":  # Ersetze "dein_passwort" mit deinem gewünschten Passwort
            subprocess.Popen("notepad.exe")
            self.root.destroy()
        else:
            time.sleep(0.5)  # Kurze Pause, um die CPU-Auslastung zu reduzieren
            command = "start microsoft.windows.camera:"
            command2 = "taskkill /im WindowsCamera.exe /t /f"
            os.system(command)
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(0.2)
            os.system(command2)
            command3 = "rundll32.exe user32.dll,LockWorkStation"
            os.system(command3)

def monitor_notepad():
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'notepad.exe':
                proc.terminate()  # Beenden Sie den Notepad-Prozess
                root = tk.Tk()
                app = NotepadStarterApp(root)
                root.mainloop()
                return  # Beenden Sie die Überwachungsfunktion, nachdem das Passwortfenster angezeigt wurde
        time.sleep(1)  # Kurze Pause, um die CPU-Auslastung zu reduzieren

# Überwachungsfunktion starten
monitor_notepad()
