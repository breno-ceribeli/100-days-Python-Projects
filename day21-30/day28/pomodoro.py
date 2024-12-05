from tkinter import *
from datetime import timedelta
from pygame import mixer
import os

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "tomato.png")
SOUND_PATH = os.path.join(os.path.dirname(__file__), "bell_notification.wav")

# Initialize the mixer for playing sound alerts
mixer.init()
sound_alert = mixer.Sound(SOUND_PATH)

# Global variables to manage the timer state
is_timer_running = False  # Tracks if a timer is currently running
reps = 0  # Number of completed Pomodoro sessions
timer = None  # Reference to the timer object

def start_timer():
    """
    Starts the Pomodoro timer and determines the duration of the current session.
    Alternates between work sessions and breaks (short or long).
    """
    global is_timer_running, reps
    if is_timer_running:  # Prevent multiple timers from running simultaneously
        return
    
    reps += 1
    is_timer_running = True

    # Set timer duration and label based on the session type
    if reps % 2 != 0:  # Odd reps: Work session
        total_time = timedelta(minutes=WORK_MIN)
        timer_title.config(text="Work", fg=GREEN)
    elif reps == 8:  # Every 8th session: Long break
        total_time = timedelta(minutes=LONG_BREAK_MIN)
        timer_title.config(text="Break", fg=RED)
        reps = 0  # Reset reps after a long break
    else:  # Even reps: Short break
        total_time = timedelta(minutes=SHORT_BREAK_MIN)
        timer_title.config(text="Break", fg=PINK)
    
    count_down(total_time)

def count_down(time_left):
    """
    Handles the countdown for the timer and updates the UI.
    Plays a sound alert and starts the next session when the timer ends.
    """
    global is_timer_running, reps, timer

    # Format and display the remaining time
    minutes, seconds = divmod(time_left.seconds, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    
    if time_left > timedelta(seconds=0):  # Continue countdown
        new_time = time_left - timedelta(seconds=1)
        timer = window.after(1000, count_down, new_time)  # Schedule the next update
    else:  # Timer finished
        canvas.itemconfig(timer_text, text="00:00")
        is_timer_running = False
        check_marks = "✔" * ((reps + 1) // 2)  # Update check marks for completed work sessions
        check_marks_label.config(text=f"{check_marks}")
        sound_alert.play()
        start_timer()  # Start the next session

def reset_timer():
    """
    Resets the timer, cancels the ongoing countdown, and clears the UI.
    """
    global timer, reps, is_timer_running
    if timer is not None:
        window.after_cancel(timer)  # Cancel the scheduled countdown
        canvas.itemconfig(timer_text, text="00:00")
        timer_title.config(text="Timer", fg=GREEN)
        check_marks_label.config(text="")
        timer = None
        reps = 0
        is_timer_running = False


# Create the main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=512, height=450)

# Timer title label
timer_title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(row=0, column=1)

# Canvas for the tomato image and timer
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=IMAGE_PATH)
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), cursor="hand2", relief=RIDGE, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), cursor="hand2", relief=RIDGE, command=reset_timer)
reset_button.grid(row=2, column=3)

# Check marks for completed cycles
check_marks_label = Label(text="", font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
check_marks_label.grid(row=3, column=1)

# Start the Tkinter event loop
window.mainloop()
