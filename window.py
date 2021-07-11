from tkinter import *
from tkinter import filedialog
import pyautogui
import numpy as np
import cv2
import os

def btn_clicked():
    print("Button Clicked")

    # USE THIS WEBSITE FOR CONVERSION OF YOUR IMAGE FIRST https://online.rapidresizer.com/photograph-to-pattern.php
    # Best to create something with sharp and clean lines, as little texture as possible
    global imageChosen
    image_name = imageChosen

    src = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)

    # Percent by which the image is resized
    scale_percent = int(entry1.get() or 100)

    # Calculate the percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # Wanted dimensions
    dsize = (width, height)

    # Resize image
    output = cv2.resize(src, dsize)

    cv2.imwrite('resized.png', output)

    # make image monochrome
    image = cv2.imread('resized.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    threshold_level = int(entry3.get() or 150)

    coords = np.column_stack(np.where(gray < threshold_level))

    size = int(len(coords))

    y_increase = int(entry4.get() or 220)
    x_increase = int(entry5.get() or 150)

    # Adjust these to center the printing of the image
    for i in range(0, size):
        # y value
        coords[i][0] = coords[i][0] + y_increase
        # x value
        coords[i][1] = coords[i][1] + x_increase

    # getting screen dimensions
    screen_width, screen_height = pyautogui.size()

    y_min = 200
    y_max = screen_height - 100
    x_min = 100
    x_max = screen_width - 100

    # this is resolution
    resolution = int(entry2.get() or 5)

    def placeDotCool(array):
        for i in range(0, size, resolution):
            if y_min < array[i][0] < y_max and x_min < array[i][1] < x_max:
                pyautogui.click(array[i][1], array[i][0])
                # print("x: {} y: {}".format(array[i][1], array[i][0]))

    # This is just FYI
    # print("Coord Size: {}".format(size))

    # initial click to change tabs:
    # make sure you have chrome in the background and run the script on the right hand of the screen
    pyautogui.click(10, 100)

    # print image
    placeDotCool(coords)

def openfile():
    global imageChosen
    imageChosen = filedialog.askopenfilename(initialdir="/",
                                       title="Select an Image",
                                       filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    # Label for Image name
    label = os.path.split(imageChosen)[1]
    text1 = Label(window, text=f"{label}")
    text1.place(x=570, y=180)

    return imageChosen


global imageChosen
imageChosen = ""

window = Tk()


window.title('Build Bot')
icon = Image("photo", file="star.gif")
window.call('wm','iconphoto', window._w, icon)

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    453.5, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    717.5, 189.5,
    image = entry0_img)

b1 = Button(
    image = entry0_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = openfile,
    relief = "flat")

b1.place(
    x = 563.0, y = 168,
    width = 309.0,
    height = 41)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    611.5, 278.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    fg = "black",
    highlightthickness = 0)

entry1.place(
    x = 563.0, y = 257,
    width = 97.0,
    height = 41)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    749.5, 278.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    fg = "black",
    highlightthickness = 0)

entry2.place(
    x = 701.0, y = 257,
    width = 97.0,
    height = 41)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    611.5, 427.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    fg="black",
    highlightthickness = 0)

entry3.place(
    x = 563.0, y = 406,
    width = 97.0,
    height = 41)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    751.5, 427.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    fg="black",
    highlightthickness = 0)

entry4.place(
    x = 703.0, y = 406,
    width = 97.0,
    height = 41)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    887.5, 427.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    fg="black",
    highlightthickness = 0)

entry5.place(
    x = 839.0, y = 406,
    width = 97.0,
    height = 41)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 691, y = 487,
    width = 117,
    height = 43)


window.resizable(False, False)
window.mainloop()
