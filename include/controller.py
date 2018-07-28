#File name: controller.py
#Author: Luke Morrow
#Date Created: 7/16/2018
#Python Version: 3.6
import os
import tkinter as tk
import include.model as model
import include.view as view

class Controller(object):
    def __init__(self):
        self.model = model.Model()
        self.view = view.View(self)

    def findShortest(self, source, dest):
        return self.model.findShortest(source, dest)

if __name__ == "__main__":
    controller = Controller()
    tk.mainloop()
