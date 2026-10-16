Terminal Speed Typing Test
A clean, lightweight, and interactive terminal-based speed typing test written in Python using the curses library. Test your typing speed in real-time with color-coded feedback for correct and incorrect characters!

Features
Real-time WPM Calculation: Computes your Words Per Minute dynamically as you type.

Instant Visual Feedback: Correctly typed characters appear in green, while errors are highlighted in red.

Non-blocking Input: Smooth, responsive typing loop utilizing curses nodelay mode.

Cross-platform Support: Works seamlessly on Linux, macOS, and Windows.

Prerequisites & Installation
Make sure you have Python installed on your system.

1. Clone or Download the Script
Save the Python script to your local machine (e.g., as typing_test.py).

2. Install Dependencies (Windows Only)
The standard Python library includes curses on Unix/Linux and macOS. If you are running Windows, you will need the windows-curses package to make it work:

Bash
pip install windows-curses
How to Run
Open your terminal or command prompt, navigate to the directory where your script is saved, and run:

Bash
python typing_test.py
Press any key on the welcome screen to begin.

Type the target sentence: "The quick brown fox jumps over the lazy dog".

Press the Esc key at any time to quit early.

Once completed, your final WPM will be displayed, and you can press any key to exit.

Future Improvements
Accuracy Tracking: Display a percentage score tracking correct vs. incorrect keystrokes.

Dynamic Sentence Generation: Pull from a randomized pool of sentences or paragraphs.

Restart Menu: Give options to restart or quit upon completion instead of closing automatically.
