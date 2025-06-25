#!/usr/bin/env python3
"""
hotkey-cleaner.py - A background service that listens for a global hotkey
to clean the clipboard text and sends a desktop notification.
"""
import re
import sys
import pyperclip
from pathlib import Path
from pynput import keyboard
from notifypy import Notify
import time

# --- Main Cleaner Class ---
class TextCleaner:
    def __init__(self):
        self.patterns_to_remove = [r'<button.*?</button>', r'<svg.*?</svg>', r'<script.*?</script>', r'<style.*?</style>', r'']
        self.invisible_chars = {'\u200B', '\u200C', '\u200D', '\u2060', '\uFEFF', '\u00A0'}

    def clean_source_text(self, text):
        if not isinstance(text, str): return ""
        for char in self.invisible_chars:
            text = text.replace(char, '')
        text = re.sub(r'<[^>]+>', '', text, flags=re.DOTALL)
        for pattern in self.patterns_to_remove:
            text = re.sub(pattern, '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text.strip()

# --- Hotkey and Notification Logic ---
HOTKEY_COMBINATION = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('m')}
pressed_keys = set()

def send_notification(title, message):
    try:
        notification = Notify()
        notification.title = title
        notification.message = message
        notification.application_name = "Clipboard Cleaner"
        notification.send(block=False)
    except Exception:
        # Fails silently if notification system is unavailable
        pass

def clean_clipboard_action():
    cleaner = TextCleaner()
    try:
        original_text = pyperclip.paste()
        if original_text and original_text.strip():
            cleaned_text = cleaner.clean_source_text(original_text)
            pyperclip.copy(cleaned_text)
            send_notification("Clipboard Cleaned", "Text is ready to be pasted.")
        else:
            send_notification("Clipboard Empty", "There was no text to clean.")
    except Exception as e:
        send_notification("Clipboard Error", f"Could not process text: {str(e)}")

def on_key_press(key):
    if key in HOTKEY_COMBINATION:
        pressed_keys.add(key)
        if all(k in pressed_keys for k in HOTKEY_COMBINATION):
            clean_clipboard_action()

def on_key_release(key):
    try:
        pressed_keys.remove(key)
    except KeyError:
        pass

if __name__ == "__main__":
    # This keeps the script running forever, listening for the hotkey.
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()
