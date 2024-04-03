import curses
from transformers import pipeline
import time


pipe = pipeline("text-generation", model="postbot/gpt2-medium-emailgen", max_new_tokens = 7)

print("model loaded")
def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.addstr(0, 0, "Enter text (Press '*' to quit): ")
    stdscr.refresh()

    user_input = ""
    while True:
        c = stdscr.getch()
        if c == ord('*'):
            break
        elif c == 32:  # Enter key
            user_input += chr(c)
            with open("output.txt", "w", encoding="utf-8") as f:
                f.write(pipe(user_input)[0]['generated_text'] + "\n")
            stdscr.clear()
            stdscr.addstr(0, 0, user_input)
            stdscr.refresh()
        else:
            user_input += chr(c)
            with open("output.txt", "w") as f:
                f.write(user_input)
            stdscr.clear()
            stdscr.addstr(0, 0, user_input)
            stdscr.refresh()
        #     user_input = ""
        # else:
        #     user_input += chr(c)
        #     stdscr.addch(1, len(user_input) - 1, chr(c))
        #     stdscr.refresh()

curses.wrapper(main)
