import tkinter as tk
from PIL import Image, ImageTk
import os
import random

def show_meme(label):
    memes_folder = "" # Put path to your memes folder here

    random_number = random.randint(1, 34)  
    meme_filename = f"meme{random_number}.png" 
    meme_path = os.path.join(memes_folder, meme_filename)

    if not os.path.exists(meme_path):
        print(f"File {meme_filename} does not exist!")
        return

    meme_image = Image.open(meme_path)
    meme_image = meme_image.resize((400, 400))  
    meme_photo = ImageTk.PhotoImage(meme_image)

    label.config(image=meme_photo, borderwidth=0) 
    label.image = meme_photo

def main():
    root = tk.Tk()
    root.title("dAiLy DoSe oF mEMeS")
    root.geometry("800x700") 

    backgrounds_folder = "" # Put path to your backgrounds folder here
    background_filename = "background_memes.jpeg" 
    background_path = os.path.join(backgrounds_folder, background_filename)

    if not os.path.exists(background_path):
        print(f"Background file {background_filename} does not exist!")
        return

    background_image = Image.open(background_path)
    background_image = background_image.resize((800, 700)) 
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)  
    background_label.image = background_photo 

    buttons_folder = ""  # Put path to your buttons folder here
    up_button_path = os.path.join(buttons_folder, "up_button.png")
    down_button_path = os.path.join(buttons_folder, "down_button.png")

    if not os.path.exists(up_button_path) or not os.path.exists(down_button_path):
        print("Button images not found!")
        return

    up_button_image = Image.open(up_button_path)
    down_button_image = Image.open(down_button_path)
    up_button_photo = ImageTk.PhotoImage(up_button_image)
    down_button_photo = ImageTk.PhotoImage(down_button_image)

    meme_label = tk.Label(root, borderwidth=0)  
    meme_label.place(x=200, y=100) 

    def on_press():
        button.config(image=down_button_photo)  
        show_meme(meme_label)  

    def on_release():
        button.config(image=up_button_photo) 

    button = tk.Button(root, image=up_button_photo, borderwidth=0, highlightthickness=0)  
    button.place(x=350, y=550)  

    # Bind press and release events
    button.bind("<ButtonPress-1>", lambda event: on_press())
    button.bind("<ButtonRelease-1>", lambda event: on_release())

    root.mainloop()

if __name__ == "__main__":
    main()
