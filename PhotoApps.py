#helps us create the GUI
import tkinter as tk

#filedialog will allow us to pick the apps and Text will help us display some text
from tkinter import filedialog, Text       

#allows us to run the apps
import os, sys, subprocess

#the root holds the app so when u want to add a button/text/frame etc u attach it to the root
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", title = "Select File",
                            filetypes=(("executables" , ".app"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()


def runApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])


canvas = tk.Canvas(root, height = 150, width = 650, bg = "#fff8e7")

#have to attach the canvas or else it wont appear
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth  = 0.8, relheight=0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open File",padx=10, 
                           pady = 5, fg = "white", bg = "#263D42", command = addApp)
openFile.pack()

runApps = tk.Button(root, text = "Run Apps",padx=10, pady = 5, 
                    fg = "white", bg = "#263D42", command = runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')