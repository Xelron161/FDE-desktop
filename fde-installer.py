import tkinter as tk
import os

def install():
    tk.Label(page2, text="Preparing...").pack()
    root.update()

    os.system("sudo apt install -y git")

    tk.Label(page2, text="Installing LightDM...").pack()
    root.update()

    os.system("sudo apt install -y lightdm")

    tk.Label(page2, text="Cloning FDE...").pack()
    root.update()

    os.system("git clone https://github.com/Xelron161/FDE-desktop")

    tk.Label(page2, text="Installing package...").pack()
    root.update()

    os.system("sudo dpkg -i FDE-desktop/fde.deb")

    tk.Label(page2, text="Fixing dependencies...").pack()
    root.update()

    os.system("sudo apt --fix-broken install -y")

    tk.Label(page2, text="Done!", font=("Segoe UI", 16)).pack()
    tk.Label(page2, text="Reboot and select FDE at login.").pack()


root = tk.Tk()
root.geometry("400x300")
root.title("FDE Installer Wizard")

page1 = tk.Frame(root)
page2 = tk.Frame(root)

for p in (page1, page2):
    p.place(relwidth=1, relheight=1)

tk.Label(page1, text="Welcome to FDE Installer Wizard!", font=("Segoe UI", 20)).pack()
tk.Label(page1, text="This Wizard is going to install FDE! 🪄", font=("Segoe UI", 10)).pack()

tk.Button(page1, text="Next", command=lambda: page2.tkraise()).pack(side="bottom", anchor="e")

tk.Label(page2, text="Click Install!", font=("Segoe UI", 20)).pack()
tk.Button(page2, text="Install", command=install).pack(side="bottom", anchor="e")

page1.tkraise()
root.mainloop()
