
# Terminal Speed Typing Test ⌨️

A clean, lightweight, and interactive terminal-based speed typing test built in Python using the `curses` library. Test your typing speed in real time with dynamic WPM tracking and instant color-coded text feedback!

---

## 🌟 Features

- **Real-Time WPM Metrics:** Calculates your Words Per Minute dynamically as you type.
- **Visual Feedback:** 
  - 🟩 **Green text:** Correctly typed characters.
  - 🟥 **Red text:** Mistakes/typos.
- **Cross-Platform Compatibility:** Runs on Linux, macOS, and Windows.
- **Smooth Performance:** Uses non-blocking keyboard input (`nodelay`) for responsive typing.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your computer.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/terminal-speed-typing-test.git
   cd terminal-speed-typing-test
   ```

2. **Windows Users Only:**
   The standard `curses` module comes pre-installed on Linux and macOS. If you are on Windows, install `windows-curses`:
   ```bash
   pip install windows-curses
   ```

---

## 🎮 How to Play

1. Run the script:
   ```bash
   python typing_test.py
   ```
2. Press **any key** on the start screen to begin the test.
3. Type out the prompt sentence as accurately and quickly as you can.
4. Use **Backspace** to fix mistakes, or press **ESC** at any time to exit.
5. Once complete, view your final WPM score and press any key to close!

---

## 🛠️ Code Overview

- `Startscreen()`: Displays the welcome interface and waits for user input.
- `display_text()`: Handles line rendering and color-coded character comparisons on screen.
- `wpm_test()`: Manages the core game loop, input detection, and time-elapsed WPM calculations.

---

## 📌 Future Enhancements

- [ ] Add accuracy percentage tracking (%)
- [ ] Support random sentences or custom text files
- [ ] Add a replay/restart option at the end screen
- [ ] Save high scores locally

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
