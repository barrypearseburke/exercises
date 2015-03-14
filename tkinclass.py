__author__ = 'Barry'
from tkinter import *
from tkinter import  filedialog,messagebox
from tkinter import ttk

class MyGUI:
    def __init__(self,parent):
        self.parent =parent

        #close
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destory)

        self.parent.option_add("*tearOff",FALSE)

        #set up menu

        self.menu =Menu(self.parent)

        self.file_menu=Menu(self.menu)
        self.file_menu.add_command(label ="open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label ="exit",command =self.catch_destory)
        self.menu.add_cascade(label ="file", menu=self.file_menu)

        self.parent.config(menu=self.menu)

        self.frame1 =ttk.Frame(parent, padding =5, border =1)
        self.frame1.grid(row=0,colum =0)
        self.chosen_file =StringVar()
        self.label1 =ttk.Label(self,frame1,textvaraible=self.file_chosen)
        self.grid(row=0,column=0,sticky=W+E)#places in midle


        ##missing code.... to open file...


    def open_file(self):
            pass

    def catch_destory(self):
        if messagebox.askokcancel("quit","do you really want to quit"):
            self.parent.destory()





def main():
    root = Tk()
    MyGUI(root)
    root.mainloop()


if __name__ =="__main__":
    main()
