import curses
from curses import wrapper
import time

def Startscreen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome To The Speed Typing Test!")
    stdscr.addstr("\nPress Any Key To Begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target_text, current_text, wpm):
    # Print the baseline target text
    stdscr.addstr(0, 0, target_text)
    
    # Overlay the colored user-typed text directly on top
    for i, char in enumerate(current_text):
        correct_char = target_text[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
        
    # Print the WPM metric below the text
    stdscr.addstr(2, 0, f"WPM: {wpm}")
    stdscr.refresh()

def wpm_test(stdscr):
    target_text = "The quick brown fox jumps over the lazy dog"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        # Prevent division by zero errors
        time_elapsed = max(time.time() - start_time, 0.1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        
        # Clear once per frame loop
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
            
        try:
            key = stdscr.getkey()
        except:
            continue
            
        # Escape key to exit
        if ord(key) == 27:
            break
            
        # Handle Backspace variations across platforms
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    Startscreen(stdscr)
    wpm_test(stdscr)
    
    # Pause at the end screen so user can see final results
    stdscr.addstr(4, 0, "Test completed! Press any key to exit.")
    stdscr.nodelay(False)
    stdscr.getkey()

wrapper(main)
