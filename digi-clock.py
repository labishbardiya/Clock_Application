import tkinter as tk
from tkinter.font import Font
import subprocess
from os.path import dirname, join

def run_script(script_name):
    current_directory = dirname(__file__)
    script_path = join(current_directory, f"{script_name}.py")
    subprocess.Popen(["python", script_path])

def create_gui():
    root = tk.Tk()
    root.title("Digital Clock Application")
    root.geometry("600x700")
    root.minsize(600, 700)
    root.configure(bg="black")

    button_font = Font(family="Helvetica", size=12, weight="bold")
    heading_font = Font(family="Helvetica", size=20, weight="bold")

    heading_label = tk.Label(root, text="JKLU: Digital Clock Project", font=heading_font, bg="black", fg="white")
    heading_label.pack(pady=10)
    jklu_image = tk.PhotoImage(file="jklu.png")
    jklu_image_resized = jklu_image.subsample(2, 2)

    def on_button_click(script_name):
        run_script(script_name)

    jklu_label = tk.Label(root, image=jklu_image_resized)
    jklu_label.pack(pady=50)

    buttons = [
        ("Alarm Clock", "alarm"),
        ("Stopwatch", "stopwatch"),
        ("Timer", "timer"),
        ("Clock", "clock")
    ]
    for button_text, script_name in buttons:
        button = tk.Button(root, text=button_text, font=button_font,
                           command=lambda sn=script_name: on_button_click(sn),
                           width=15, height=2, bg="lightblue", fg="black",
                           relief=tk.RAISED, bd=3)
        button.pack(pady=5)

    root.mainloop()
if __name__ == "__main__":
    create_gui()