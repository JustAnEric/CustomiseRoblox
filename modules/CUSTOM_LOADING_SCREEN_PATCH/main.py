import customtkinter, pyautogui as pg, os

import tkinter as tk
from tkinter import ttk

def loading_page():

    def close_loading():
        root.destroy()
        
    root = tk.Tk()
    root.title("Loading Page")
    root.geometry("300x200")
    root.resizable(False, False)
    root.attributes('-alpha', 0.85)
    root.attributes('-toolwindow',1)
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.configure(bg="black")
    root.tk.call('tk', 'scaling', 2.0)

    def place_center():  # Placing the window in the center of the screen
        global x, y
        reso = pg.size()
        rx = reso[0]
        ry = reso[1]
        x = int((rx / 2) - (500 / 2))
        y = int((ry / 2) - (500 / 2))
        root.geometry(f"500x200+{x}+{y}")


    place_center()

    # Create a label for the loading message
    loading_label = ttk.Label(root, text="Loading Roblox...", font=("Segoe UI", 14), background="black", foreground="white")
    loading_label.pack(pady=50)

    # Create a progress bar
    progress_bar = customtkinter.CTkProgressBar(root, mode='indeterminate')
    progress_bar.pack()

    # Start the progress bar animation
    progress_bar.start()

    # Schedule closing the loading window after 5 seconds
    launch_roblox()
    root.after(10000, close_loading)
    root.mainloop()

def launch_roblox():
    PATH = "%LOCALAPPDATA%/Roblox/Versions/version-48a28da848b7420d"
    LAUNCHER = "RobloxPlayerBeta.exe"
    os.system(f"cd {PATH} && start {LAUNCHER}")

loading_page()
