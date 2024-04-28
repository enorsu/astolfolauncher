import tkinter as tk
import os
from tkinter import messagebox
import random

def generateRandomUser():
    num = "123456789069696969"
    char = "qwertyuiopasdfghjklzxcvbnm"

    random_string = ""

    for i in range(10):
        random_string = random_string +  random.choice(char)
    for i in range(4):
        random_string = random_string + random.choice(num)

    usernameValue.set(random_string)

def setJavaPath():
    javaPath.set("javaw")



def runAstolfo():

    root.withdraw()
    file = open("temprunner.bat", "w")
    file.write("@echo off" + "\n")
    file.write("set folder=%appdata%" + "\n")
    

    
    bigstring = f'{javaPath.get()} -noverify -Xms2024M -Xmx4048M -Djava.library.path="natives" -cp "libs";"release.jar" net.minecraft.client.main.Main --accessToken vcyegwgdhugegwhy --ver Astolfo --gameDir "%folder%\\.minecraft" --assetsDir "assets" --assetIndex 1.8 --username {usernameValue.get()} --launchToken a'
    file.write(bigstring + "\n")
    file.close()
    os.system("temprunner.bat")
    os.remove("temprunner.bat")

    root.deiconify()


def showInfo():

    
    root1 = tk.Tk()
    root1.title("credits")
    root1.resizable(False, False)
    info = """
Astolfo Launcher
Made by enorsu
Python 3.12.3
Alpha Build 1.6.1

Astolfo Client Crack by AllahLeaks
        """
    lbl5 = tk.Label(root1, text=info, font=("Helvetica", 10))
    lbl5.pack()

    closeInfo = tk.Button(root1, text="close", padx=15, pady=3, cursor="hand2", command=root1.destroy)
    closeInfo.pack()
    root1.mainloop()



def label_clicked(event):
    #root.withdraw()
    #messagebox.showinfo("credits", info)
    #root.deiconify()

    showInfo()



root = tk.Tk()
root.title("Astolfo Launcher")
root.geometry("300x260")
root.resizable(False,False)


usernameValue = tk.StringVar()
usernameValue.set("astolfo")

lbl1 = tk.Label(root, text="Astolfo Launcher", font=("Helvetica", 16))
lbl1.pack(anchor="center")

javaPath = tk.StringVar()
javaPath.set("javaw")


lbl2 = tk.Label(root, text="Username:")
lbl2.pack(anchor="center")

usernameInput = tk.Entry(root, textvariable=usernameValue)
usernameInput.pack(anchor="center")

#doRandomize = tk.IntVar()

#randomizeUserCheckbox = tk.Checkbutton(root, text="Randomize username", variable=doRandomize)
#randomizeUserCheckbox.pack(anchor="center")

runBtn = tk.Button(root, text="Run", padx=15, pady=3, cursor="hand2", command=runAstolfo)
runBtn.pack(anchor="center", pady=10)

randomizeBtn = tk.Button(root, text="Randomize username", padx=15, pady=3, cursor="hand2", command=generateRandomUser)
randomizeBtn.pack(anchor="center")


lbl3 = tk.Label(root, text="click for more info",font=("Helvetica", 9), cursor="hand2")
lbl3.pack(anchor="center", side="bottom")
lbl3.bind("<Button-1>", label_clicked)

javaInput = tk.Entry(root, textvariable=javaPath)
javaInput.pack(anchor="center", side="bottom", pady=10)

lbl4 = tk.Label(root, text="Java path:",font=("Helvetica", 9))
lbl4.pack(anchor="center", side="bottom")



root.mainloop()

