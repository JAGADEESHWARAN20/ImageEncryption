import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from tkinter import * #type:ignore
from ttkbootstrap import * #type:ignore

root = tb.Window()
root.geometry('400x500')
style = Style(theme='vapor') #type:ignore
width_of_window = 400
height_of_window = 500
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)

root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))


def encrypt_image():
  file1=filedialog.askopenfile (mode='r',filetype=[('jpg file','*.jpg','.png')]) # type: ignore
  if file1 is not None:
    file_name=file1.name
    key=entry1.get() # type: ignore
    print(file_name, key)
    fi=open(file_name, 'rb')
    image=fi.read()
    fi.close()
    image=bytearray(image)
    for index,values in enumerate(image):
      image[index]=values^int(key)
      fil=open(file_name,'wb')
      fil.write(image)
      fil.close()
      
      
def decrypt_image():
  file1=filedialog.askopenfile (mode='r',filetype=[('jpg file','*.jpg','.png')]) # type: ignore
  if file1 is not None:
    file_name=file1.name
    key=entry2.get() # type: ignore
    print(file_name, key)
    fi=open(file_name, 'rb')
    image=fi.read()
    fi.close()
    image=bytearray(image)
    for index,values in enumerate(image):
      image[index]=values^int(key)
      fil=open(file_name,'wb')
      fil.write(image)
      fil.close()


b1=Button(root, text="encrypt", command=encrypt_image)
b1.pack(side='top')
b2=Button(root, text="Decrypt", command=decrypt_image)
b2.pack(side='bottom')
entry_Label2=tb.Labelframe(root,text='Decryption')  
entry_Label2.pack(side='bottom')
entry2 = tb.Entry(entry_Label2,bootstyle='primary') #type:ignore
entry2.pack(side='bottom')
entry_Label=tb.Labelframe(root,text='Encryption') 
entry_Label.pack(side='top')
entry1=tb.Entry(entry_Label,bootstyle='secondary') #type:ignore
entry1.pack(side='top')
root.mainloop()


