from tkinter import *
import details

# Setup a screen
window = Tk()
window.title("CountDown")
window.config(padx=50, pady=50, bg=details.Yellow)

# Timing and function
def count_down(number):
    minutes = number // 60
    seconds = number % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if number >= 0:
        window.after(1000, count_down, number - 1)

def start_timer():
    count_down(25 * 60) 

def reset_timer():
    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text="00:00")

# Label
title = Label(text="Timer!", fg=details.Green, font=(details.Font_Name, details.Font_Size_Timer), bg=details.Yellow)
title.grid(column=1, row=0)

# Setup buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✅", fg=details.Green, highlightthickness=0, bg=details.Yellow)
check_marks.grid(column=1, row=2)

# Set up canvas
canvas = Canvas(width=360, height=360, highlightthickness=0, bg=details.Yellow)
image = PhotoImage(file="./count.png")
canvas.create_image(180, 180, image=image)
timer_text = canvas.create_text(180, 210, text="00:00", fill="black", font=(details.Font_Name, details.Font_Size))
canvas.grid(column=1, row=1)

# Run the Tkinter event loop
window.mainloop()
