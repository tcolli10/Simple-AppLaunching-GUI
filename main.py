from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import BOTTOM, RIGHT, TOP, Y, filedialog, Text
import os
from turtle import bgcolor


HEIGHT = 800
WIDTH = 800
BG = '#263D42'
BUTTON_COLOR = '#19A7F2'


root = tk.Tk()
apps = []
labels = []
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    file = filedialog.askopenfile(initialdir='/', title="Select File", 
                                    filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(file.name)
    for app in apps:
        label = tk.Label(frame, text= app, bg= 'grey')
        labels.append(label)
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def clearApps():
    open('save.txt', 'w').close()
    for i in range(len(apps)):
        apps.remove(apps[0])
    for label in labels:
        label.destroy()

    
canvas = tk.Canvas(root, height= HEIGHT, width=  WIDTH, bg = BG)
canvas.pack()

frame = tk.Frame(root, bg= 'white')
frame.place(relwidth= 0.8, relheight= 0.8, relx= 0.1, rely= 0.1)

openFile = tk.Button(root, text='Open File', padx= 30, 
                    pady= 5, fg= 'white', bg= BUTTON_COLOR, command= addApp)

openFile.place(x= 10, y= 760)

runAppsButton = tk.Button(root, text='Run Apps', padx= 30, 
                    pady= 5, fg= 'white', bg= BUTTON_COLOR, command= runApps)
# runApps.place(x = 340, y= 795)
runAppsButton.place(x= 355, y= 760)

clearAppsButton = tk.Button(root, text='Clear Apps', padx= 30,
                    pady= 5, fg='white', bg= BUTTON_COLOR, command= clearApps)
clearAppsButton.place(x= 670, y= 760)

titleLable = tk.Label(root, text= 'Apps List', bg= 'white')
titleLable.place(x= 380, y= 30)


for app in apps:
    label = tk.Label(frame, text= app)
    label.pack

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

