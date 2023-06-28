import tkinter as tk
from tkinter import filedialog
from tkinter import * #type:ignore
from tkinter import ttk #type:ignore
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkbootstrap as ttk


import PIL

# Create the tkinter window
root = ttk.Window()
root.geometry('400x500')
root.resizable(False, False)
style = ttk.Style("darkly")



# Calculate the coordinates for centering the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width_of_window = 400
height_of_window = 600
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

# Create a frame
frame = Frame(root, width=300, height=300)

# Calculate the coordinates to center the frame
x_coordinate_frame = (width_of_window / 2) - (frame['width'] / 2)
y_coordinate_frame = (height_of_window / 2) - (frame['height'] / 2)

# Place the frame in the center
frame.place(x=x_coordinate_frame, y=y_coordinate_frame)

label = Label(frame)

def display_image(file_name):
    # Load the image using PIL
    image = Image.open(file_name)
    
    # Resize the image to fit the frame
    image = image.resize((300, 300), Image.ANTIALIAS)
    
    # Create a Tkinter image object
    img = ImageTk.PhotoImage(image)
    
    # Create a label to display the image
    label = Label(frame, image=img)
    label.image = img  # Keep a reference to avoid garbage collection
    label.pack()

    
def encrypt_image():
    try:
      file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg'), ('png file', '*.png')])
      if file1 is not None:
          file_name = file1.name
          key = entry1.get() # Get the input value from entry1 widget
          
          fi = open(file_name, 'rb')
          image = fi.read()
          fi.close()
          
          image = bytearray(image)
          for index, values in enumerate(image):
              image[index] = values ^ int(key)
              
          fil = open(file_name, 'wb')
          fil.write(image)
          fil.close()
          
          label.pack_forget()  # Hide the original image
          
          # Display the encrypted image
          display_image(file_name)
          messagebox.showinfo("Operation Successful", "Image encrypted successfully")
    except PIL.UnidentifiedImageError:
        messagebox.showinfo("Operation Successful", "Image encrypted successfully")
      
        print("Unable to identify the image file. Please check the file format and try again.")


def decrypt_image():
    try:
      file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg'), ('png file', '*.png')])
      if file1 is not None:
          file_name = file1.name
          key = entry2.get()  # Get the input value from entry2 widget
          
          fi = open(file_name, 'rb')
          image = fi.read()
          fi.close()
          
          image = bytearray(image)
          for index, values in enumerate(image):
              image[index] = values ^ int(key)
              
          fil = open(file_name, 'wb')
          fil.write(image)
          fil.close()
          
          label.pack_forget()  # Hide the original image
          
          # Display the decrypted image
          display_image(file_name)
          messagebox.showinfo("Operation Successful", "Image decrypted successfully")
    except PIL.UnidentifiedImageError:
        print("Unable to identify the image file. Please check the file format and try again.")


def Close_window():
  root.destroy()
# Create buttons and entry fields
label = ttk.Label(root,text='Image Encryption',font=('poppins',15))
label.pack(padx=5,pady=10,side='top',anchor=NW)
b3 = Button(root, text="X", command=Close_window)
b3.pack(side='top',anchor=NE,ipadx=10,ipady=10,padx=10)
b1 = Button(root, text="Encrypt", command=encrypt_image)
b1.pack(ipadx=20,ipady=10, pady=10,side='top')
b2 = Button(root, text="Decrypt", command=decrypt_image)
b2.pack(ipadx=20,ipady=10,pady=10,side='bottom')

root.overrideredirect(1)


# Create label frame and entry widget for encryption
entry_Label = ttk.LabelFrame(root, text='Encryption')
entry_Label.pack(side='top')
entry1 = ttk.Entry(entry_Label, style='secondary.TEntry')
entry1.pack(side='top')

# Create label frame and entry widget for decryption
entry_Label2 = ttk.LabelFrame(root, text='Decryption')
entry_Label2.pack(side='bottom')
entry2 = ttk.Entry(entry_Label2, style='primary.TEntry')
entry2.pack(side='bottom')

root.mainloop()
