from tkinter import *
import datetime
import time
import pygame
from threading import *

pygame.mixer.init()

root = Tk()
root.geometry("500x650")
root.minsize(500, 650)
root.configure(bg="black")
root.title("JKLU: ALARM CLOCK")

logo_image = PhotoImage(file="jklu.png")
logo_image_resized = logo_image.subsample(4)
logo_label = Label(root, image=logo_image_resized, bg="black")
logo_label.pack(pady=10)

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        alarm_time_label.config(text=f"Alarm Time: {set_alarm_time}")  # Update alarm time label
        if current_time == set_alarm_time:
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play(loops=0)
            stop_button.config(state="normal")
            break

def cancel_alarm():
    # Stop the alarm sound
    pygame.mixer.music.stop()
    stop_button.config(state="disabled")
    # Reset the displayed alarm time to 00:00:00
    alarm_time_label.config(text="Alarm Time: 00:00:00")

def stop_alarm():
    pygame.mixer.music.stop()
    stop_button.config(state="disabled")

Label(root, text="Set Time", font=("Helvetica 15 bold"), bg="black", fg="white").pack()

frame = Frame(root, bg="black")
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = tuple(f"{i:02d}" for i in range(60))
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = tuple(f"{i:02d}" for i in range(60))
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

set_button = Button(root, text="Set Alarm", font=("Helvetica 15"), fg="black", bg="green", command=Threading)
set_button.pack(pady=20)

cancel_button = Button(root, text="Cancel Alarm", font=("Helvetica 15"), fg="black", bg="orange", command=cancel_alarm)
cancel_button.pack(pady=20)

stop_button = Button(root, text="Stop Alarm", font=("Helvetica 15"), fg="black", bg="red", command=stop_alarm, state="disabled")
stop_button.pack(pady=20)

alarm_time_label = Label(root, text="Alarm Time: --:--:--", font=("Helvetica 15"), bg="black", fg="white")
alarm_time_label.pack(pady=20)  # Add label to display alarm time

root.mainloop()