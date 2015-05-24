__author__ = 'Barry'
# Barry Burke
#c13427078
#Labtest2

#imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import os
import time
import string


class GUI():
    def __init__(self, parent):  #parent is root
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.catch_destroy)
        self.parent.option_add('*tearOff', FALSE)  #this stops the user from tearing off the menus
        self.menu = Menu(self.parent)

        self.file_menu = Menu(self.parent)
        self.file_menu.add_command(label="Open", command=self.open_file)  #call open file fxn
        self.file_menu.add_command(label="Display Metadata", command=self.metadata)  #call metadata file
        self.file_menu.add_command(label="Exit", command=self.catch_destroy)  #call metadata file

        self.menu.add_cascade(label="File",
                              menu=self.file_menu)  #will place open,metadata and exit in one drop down menu called file

        self.parent.config(menu=self.menu)
        #making a frame
        self.frame1 = ttk.Frame(parent, padding=10, border=2)
        self.frame1.grid(row=0, column=0)  #places a frame in row 0 col 0(first)

        self.chosen_file = StringVar()
        self.label1 = ttk.Label(self.frame1, text="Please Open A file by selecting it in the FILE -> Open ")
        self.label1.grid(row=0, column=0, sticky=W + E)
        self.frame2 = ttk.Frame(parent, padding=5, border=1)
        self.frame2.grid(row=1, column=0)

        self.text1 = Text(self.frame2, width=100, wrap=NONE)

        self.text1 = Text(self.frame2, width=100, wrap=NONE)
        self.yscrollbar = ttk.Scrollbar(self.frame2, orient=VERTICAL, command=self.text1.yview)
        self.yscrollbar.grid(column=1, row=1, sticky=NS)

        self.xscrollbar = ttk.Scrollbar(self.frame2, orient=HORIZONTAL, command=self.text1.xview)
        self.xscrollbar.grid(column=0, row=2, sticky=EW)

        self.text1['yscrollcommand'] = self.yscrollbar.set
        self.text1['xscrollcommand'] = self.xscrollbar.set
        self.text1.grid(row=1, column=0)

    def open_file(self):
        #self.fileopened =0
        # Can run file dialogue from anywhere
        chosen_file = filedialog.askopenfilename(filetypes=(("HTML", "*.HTML"),
                                                            ("Text files", "*.txt"),
                                                            ("All files", "*.*") ))
        #self.file =chosen_file
        #self.fileopened=1

        #metadata
        self.os =("SIZE: {} \n mode {}\n accessed {} \nlast mod {}\n".format(os.stat(chosen_file).st_ctime,os.stat(chosen_file).st_mode,os.stat(chosen_file).st_atime,os.stat(chosen_file).st_mtime))
        self.my_time = time.asctime(time.localtime(os.stat(chosen_file).st_ctime))


        self.chosen_file.set(chosen_file)

        print("Selected: {}".format(self.chosen_file.get()))

        with open(self.chosen_file.get(), "r") as input:
            file_contents = input.read()

        self.text1.insert(INSERT, file_contents)
        self.text1['state'] = 'disabled'

    def metadata(self):

                #display metadata in message box
                messagebox.askokcancel("metadata","{}Date Created ={}".format(self.os,self.my_time))






    def catch_destroy(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            if messagebox.askokcancel("Seriouly?", "But Are you really sure?"):
                if messagebox.askokcancel("PLEASE DONT", "Okay then , ill let you leave!!!"):
                    self.parent.destroy()


def main():
    root = Tk()
    root.wm_title("File Opener - Lab Test Barry Burke -C13427078 ")
    GUI(root)  # passes root to the gui class
    root.mainloop()  #keeps tk from closing


if __name__ == '__main__':
    main()
