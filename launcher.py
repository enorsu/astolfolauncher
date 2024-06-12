import os
import random
import webbrowser
import customtkinter as customtkinter  # type: ignore

# Set CustomTkinter appearance mode and color theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def generate_random_user():
    num = "1234567890"
    char = "qwertyuiopasdfghjklzxcvbnm"

    random_string = ""

    for i in range(10):
        random_string += random.choice(char)
    for i in range(4):
        random_string += random.choice(num)

    usernameValue.set(random_string)
# Function to display initial warning about RATs


def display_initial_warning():
    return customtkinter.CTkMessagebox.askyesno("Warning", "Running certain applications may expose your system to Remote Access Trojans (RATs). Exercise caution and consider installing HostsMod for additional protection.")

# Function to display second warning before running potentially risky application
def display_second_warning():
    return customtkinter.CTkMessagebox.askyesno("Warning", "You are about to run an application that may be risky. Do you want to proceed?")

# Function to prompt user to install HostsMod
def prompt_install_hostsmod():
    response = customtkinter.CTkMessagebox.askyesno("Install HostsMod", "HostsMod is not installed on your system. Do you want to install it for additional protection?")
    if response:
        # Open the browser to download HostsMod
        webbrowser.open("https://github.com/GardeningTool/HostsMod/releases/tag/2.0.1/HostsMod.exe")

# Function to run Astolfo application
def run_astolfo():
    if display_initial_warning():
        if display_second_warning():
            prompt_install_hostsmod()
            # Proceed with running Astolfo application
            with open("temprunner.bat", "w") as file:
                file.write("@echo off\n")
                file.write("set folder=%appdata%\n")

                bigstring = f'{javaPath.get()} -noverify -Xms2024M -Xmx4048M -Djava.library.path="natives" -cp "libs";"release.jar" net.minecraft.client.main.Main --accessToken vcyegwgdhugegwhy --ver Astolfo --gameDir "%folder%\\.minecraft" --assetsDir "assets" --assetIndex 1.8 --username {usernameValue.get()} --launchToken a' # type: ignore
                file.write(bigstring + "\n")
            
            os.system("temprunner.bat")
            os.remove("temprunner.bat")

# Function to display credits and information
def show_info():
    root1 = customtkinter.CTk()
    root1.title("Information")
    root1.geometry("250x250")  # Set the window size to 200x200
    root1.resizable(True, True)

    info = """
Unofficial Launcher For CRACKED Astolfo
Made by enorsu
Reworked by Panagiotis3149
Python 3.12.4/3.12.3
Alpha Build 1.7.3

Astolfo Client Crack by AllahLeaks
    """

    info_box = customtkinter.CTkTextbox(root1, width=250, height=250)  # Create a textbox with 250x250 size
    info_box.insert("0.0", info)
    info_box.configure(state="disabled")  # Make the textbox read-only
    info_box.pack(pady=10, padx=10)

    close_info_btn = customtkinter.CTkButton(root1, text="Close", width=120, height=32, cursor="hand2", command=root1.destroy)
    close_info_btn.pack(pady=10, padx=10)
    
    root1.mainloop()

def label_clicked():
    show_info()

# Create the root window
root = customtkinter.CTk()
root.title("Astolfo Launcher")
root.geometry("390x250")
root.resizable(False, False)

usernameValue = customtkinter.StringVar(value="AstolfoRATTED")

# Username Label and Entry
username_label = customtkinter.CTkLabel(root, text="Username:")
username_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

usernameInput = customtkinter.CTkEntry(root, textvariable=usernameValue)
usernameInput.grid(row=0, column=1, padx=20, pady=10)

# Launch Astolfo Button
launch_button = customtkinter.CTkButton(root, text="Launch Astolfo", cursor="hand2", command=run_astolfo)
launch_button.grid(row=3, column=1, padx=20, pady=10)

launch_button = customtkinter.CTkButton(root, text="Randomize Username", cursor="hand2", command=generate_random_user)
launch_button.grid(row=1, column=1, padx=20, pady=10)

# Info Button
info_button = customtkinter.CTkButton(root, text="Info", cursor="hand2", command=label_clicked, fg_color="#379634")
info_button.grid(row=4, column=1, padx=20, pady=10)

root.mainloop()
