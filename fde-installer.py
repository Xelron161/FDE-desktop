import tkinter as tk
from tkinter import ttk
import os
import threading

def install():
    steps = [
        ("Preparing...", "sudo apt install -y git"),
        ("Installing LightDM...", "sudo apt install -y lightdm"),
        ("Cloning FDE...", "git clone https://github.com/Xelron161/FDE-desktop"),
        ("Installing package...", "sudo dpkg -i FDE-desktop/fde.deb"),
        ("Fixing dependencies...", "sudo apt --fix-broken install -y")
    ]

    progress["maximum"] = len(steps)

    for i, (text, cmd) in enumerate(steps, start=1):
        status_label.config(text=text)
        root.update()

        os.system(cmd)

        progress["value"] = i
        root.update()

    status_label.config(text="Done!")
    tk.Label(page2, text="Reboot and select FDE at login.").pack()


def start_install():
    threading.Thread(target=install).start()


root = tk.Tk()
root.geometry("400x300")
root.title("FDE Installer Wizard")

page1 = tk.Frame(root)
page2 = tk.Frame(root)

for p in (page1, page2):
    p.place(relwidth=1, relheight=1)

tk.Label(page1, text="Welcome to FDE Installer Wizard!", font=("Segoe UI", 20)).pack()
tk.Label(page1, text="This Wizard is going to install FDE! 🪄").pack()

tk.Button(page1, text="Next", command=lambda: page2.tkraise()).pack(side="bottom", anchor="e")

tk.Label(page2, text="Click Install!", font=("Segoe UI", 20)).pack()

status_label = tk.Label(page2, text="")
status_label.pack(pady=10)

progress = ttk.Progressbar(page2, length=250, mode="determinate")
progress.pack(pady=10)

tk.Button(page2, text="Install", command=start_install).pack(side="bottom", anchor="e")

page1.tkraise()
root.mainloop()

