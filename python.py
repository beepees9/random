# Import the modules
import tkinter as tk  1
import time 1

# Create the main window
window = tk.Tk()
window.title("Cookie Clicker")
window.geometry("400x300")

# Create the cookie image
cookie = tk.PhotoImage(file="cookie.png")

# Create the variables
cookies = 0 # The number of cookies
cps = 0 # The cookies per second
click_value = 1 # The value of each click
upgrades = [] # The list of upgrades

# Define the functions
def update():
    """Update the cookies and the labels every second"""
    global cookies
