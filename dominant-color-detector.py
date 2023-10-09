import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

def detect_color():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = cv2.resize(image, (400, 300))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image_rgb)
        img = ImageTk.PhotoImage(img)

        image_label.config(image=img)
        image_label.image = img

        average_color = np.mean(image, axis=(0, 1))
        dominant_color = tuple(map(int, average_color))
        result_label.config(text=f"Dominant Color: {dominant_color}")

root = tk.Tk()
root.title("Color Detection")

file_button = ttk.Button(root, text="Open Image", command=detect_color)
file_button.pack(pady=10)

image_label = ttk.Label(root)
image_label.pack()

result_label = ttk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

root.mainloop()
