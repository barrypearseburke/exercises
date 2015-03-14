__author__ = 'Barry'
from tkinter import*
from tkinter import  filedialog,messagebox
from tkinter import ttk

class GUI():
    def __init__(self,my_parent):
        self.my_parent = my_parent
        self.my_parent.title("Feet to Meter Conversation") #This is bar at top on the line with the x to close
        self.frame = Frame(self.my_parent)
        self.frame.grid(row=0,column=0)


        self.entry1 = Entry(self.my_parent)
        self.entry1.grid(row=0,column=1)

        self.label =Label(self.my_parent, text ="feet")
        self.label.grid(row=0,column=2)

        self.labe2 =Label(self.my_parent, text ="equals = ")
        self.labe2.grid(row=1,column=0)

        self.labe3 =Label(self.my_parent, text ="meters")
        self.labe3.grid(row=1,column=2)



        self.answer =StringVar()
        self.label4=Label(self.my_parent,textvariable = self.answer)
        self.answer.set("")
        self.label4.grid(row=1,column=1)



        self.button = Button(self.my_parent, text ="enter",command =self.cal)
        self.button.grid(row=2,column=1)

    def cal(self):
        feet = self.entry1.get()
        meters =int(feet)*0.3048
        self.answer.set(meters)


def main():
    root = Tk()

    myapp =GUI(root)

    root.mainloop()
if __name__ =="__main__":
    main()