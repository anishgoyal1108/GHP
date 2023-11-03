import os
import tkinter as tk
from PIL import Image, ImageTk

image_folder = "C:/Users/Anish/Downloads/pics"  # Path to your image folder
images = []
current_image_index = 0

def load_images(folder):
    image_list = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as needed
            image_path = os.path.join(folder, filename)
            image = Image.open(image_path)
            image_list.append(image)
    return image_list

def update_image():
    global current_image_index
    image = images[current_image_index]
    image = image.resize((800, 600))  # Adjust the size of the displayed image
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo  # Store the reference to prevent image garbage collection

def next_image(event=None):
    global current_image_index
    current_image_index = (current_image_index + 1) % len(images)
    update_image()

def prev_image(event=None):
    global current_image_index
    current_image_index = (current_image_index - 1) % len(images)
    update_image()

window = tk.Tk()
window.title("Image Slideshow")
window.geometry("800x600")  # Set your desired window dimensions

images = load_images(image_folder)
total_images = len(images)

image_label = tk.Label(window)
image_label.pack()

window.bind("<Right>", next_image)
window.bind("<Left>", prev_image)

update_image()

window.mainloop()
