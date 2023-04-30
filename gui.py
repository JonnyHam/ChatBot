from tkinter import *
from PIL import ImageTk, Image

from chatbot import guireturn

root = Tk()
root.geometry("300x300")
root.title("Afghan Hound Chatbot")
root.configure(bg='Peru')

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    Output.delete(1.0,END)
    Output.insert(END, guireturn(INPUT) + "\n")



l = Label(text="Afghan Hound Chatbot")
l.configure(bg='BurlyWood')
img = Image.open("AfghanHound.jpg")
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo).place(x=50,y=50)
inputtxt = Text(root, height=5,
                width=20,
                bg="SaddleBrown",
                fg="PapayaWhip")


Output = Text(root, height=10,
              width=50,
              bg="Bisque")

Display = Button(root, height=2,
                 width=20,
                 text="Ask the Afghan Hound!",
                 command=lambda: Take_input(),
                 bg="BurlyWood")

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()



