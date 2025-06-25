Markdown

# Hotkey Clipboard Cleaner

A background service to instantly clean and sanitize text on your clipboard via a global hotkey (`Ctrl+M`).

## The Problem

When you copy text from AI chats (like ChatGPT, Gemini) or modern web pages, you are often copying more than just the visible text. This "invisible junk" can include:

- **HTML Tags:** Buttons, divs, and other formatting that breaks plain text pasting.
- **Tracking Characters:** Invisible Unicode characters (zero-width spaces, etc.) that can be used as a "watermark" to track the origin of the text, potentially identifying it as AI-generated.
- **Styles and Scripts:** Unnecessary code that can cause issues in many editors.

This tool was created to solve that problem by acting as an intermediary: you copy the messy text, press a hotkey, and the text in your clipboard becomes 100% clean and safe to paste anywhere.

## Features

- **Global Hotkey:** Activate the cleaning process from any application by pressing `Ctrl+M`. It integrates directly into your workflow.
- **Deep Text Cleaning:** Removes a wide range of invisible Unicode characters, HTML tags, and other web annoyances.
- **Code Block Preservation:** Intelligently detects and preserves code blocks (formatted with ```) so they are not destroyed during the cleaning process.
- **Desktop Notifications:** Provides instant visual feedback to confirm that the clipboard has been successfully cleaned.
- **Silent Background Operation:** Runs as a persistent background service, starting automatically with your system.

## Requirements

- Python 3.8+
- `pip` (Python package installer)
- **For Linux:** A clipboard utility. `xclip` is recommended.
 ```bash
 sudo apt-get install xclip

Installation

These steps describe how to set up the project on a Linux-based system.

1. Create Project Files

In your project folder, create two files: hotkey-cleaner.py and requirements.txt.

 hotkey-cleaner.py: The code for this file can be found in our previous conversation. It's the main Python script for the service.

 requirements.txt:

 pyperclip
 pynput
 notify-py

2. Set Up Virtual Environment

It is best practice to use a virtual environment (venv) to keep dependencies isolated.
Bash

# Navigate to your project folder
cd /path/to/your/project

# Create the virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

3. Install Dependencies

With your virtual environment active, install the required libraries:
Bash

pip install -r requirements.txt

Setup: Running as a Background Service

To make the script run automatically every time you log in, add it to your desktop environment's startup applications.

 Find Startup Applications: Search for "Startup Applications" in your system's application menu.

 Add a New Entry: Click "Add" and fill in the fields:

 Name: Hotkey Clipboard Cleaner

 Comment: Cleans clipboard text using Ctrl+M

 Command: You must provide the full, absolute paths to both the Python executable inside your venv and the script itself. For example:

 /home/user/my-project/venv/bin/python3 /home/user/my-project/hotkey-cleaner.py

 Save and Restart: Save the new startup entry. Log out and log back in for the change to take effect.

Usage

The workflow is designed to be seamless and invisible.

 Copy Text: Select any text and copy it (Ctrl+C).

 Press Hotkey: Press Ctrl+M. A desktop notification will confirm the action.

 Paste Clean Text: Paste the text anywhere (Ctrl+V). It will be perfectly clean.

Future Enhancements

The current cleaning process is literal—it removes unwanted characters and formatting. A future version could incorporate a Small Language Model (SLM) to paraphrase the text. This would help to further "humanize" the text and make its AI origin even less detectable.
