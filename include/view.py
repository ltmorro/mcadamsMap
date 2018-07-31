#!/usr/bin/python3.5

import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import collections

WIDTH = 1024
HEIGHT = 1024
class Controller(object):
    def __init__(self):
        pass

    def findShortest(self, source, dest):
        print("Finding path from: " + source + " to " + dest)

class View(object):
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("McAdams Hall Map")
        self.root.bind("<Return>", lambda e: self.findShortest(self.sourceVar.get(), self.destVar.get()))
        self.sourceVar = tk.StringVar()
        self.destVar = tk.StringVar()
        self.selection = tk.Frame(self.root, width=WIDTH, height=HEIGHT/4)
        self.selection.pack(side=tk.TOP)
        self.sourceBut = tk.Button(self.selection, text="Select Starting Point", command=self.selectSource)
        self.sourceBut.pack(side=tk.LEFT)
        self.source = tk.Entry(self.selection, text=self.sourceVar)
        self.source.pack(side=tk.LEFT)
        self.destBut = tk.Button(self.selection, text="Select Destination", command=self.selectDest)
        self.destBut.pack(side=tk.LEFT)
        self.dest = tk.Entry(self.selection, text=self.destVar)
        self.dest.pack(side=tk.LEFT)
        self.search = tk.Button(self.selection, text="Find Directions", command=lambda: self.findShortest(self.sourceVar.get(), self.destVar.get()))
        self.search.pack(side=tk.LEFT)
        self.nb = ttk.Notebook(self.root)
        self.nb.pack()
        #self.rooms follow format upper left coord, lower right coord
        #in inches [x1, y1, x2, y2]
        elevator = collections.defaultdict(list)
        self.rooms = collections.defaultdict(list)
        hallways = collections.defaultdict(list)
        hallways2 = collections.defaultdict(list)
        hallways3 = collections.defaultdict(list)
        self.rooms2 = collections.defaultdict(list)
        self.rooms3 = collections.defaultdict(list)
        closets = collections.defaultdict(list)
        closets2 = collections.defaultdict(list)
        closets3 = collections.defaultdict(list)
        stairs1 = collections.defaultdict(list)
        stairs2 = collections.defaultdict(list)
        stairs3 = collections.defaultdict(list)
        self.rooms["101"] = [2.101, 6.868, 2.693, 7.459, "left"]
        self.rooms["102"] = [1.103, 6.808, 1.843, 7.445, "right"]
        self.rooms["103"] = [2.101, 6.402, 2.485, 6.868, "left"]
        self.rooms["104"] = [1.103, 6.179, 1.843, 6.808, "right"]
        self.rooms["105"] = [2.101, 5.710, 2.485, 6.402, "left"]
        self.rooms["106"] = [1.103, 5.710, 1.843, 6.179, "right"]
        self.rooms["107"] = [2.101, 5.24, 2.485, 5.710, "left"]
        self.rooms["108"] = [1.103, 5.24, 1.843, 5.710, "right"]
        self.rooms["109"] = [.905, 4.198, 1.408, 4.955, "right"]
        self.rooms["110B"] = [1.408, 1.561, 2.460, 2.666, "bottom"]
        self.rooms["110C"] = [2.460, 1.561, 2.974, 2.666, "bottom"]
        self.rooms["110D"] = [3.394, 1.561, 4.41, 2.92, "left"]
        self.rooms["110E"] = [3.394, 2.92, 4.41, 4.198, "left"]
        self.rooms["110A"] = [1.408, 2.666, 3.394, 4.198, "bottom"]
        self.rooms["111"] = [2.905, 5.24, 3.333, 5.710, "right"]
        self.rooms["112"] = [3.936, 4.198, 4.600, 4.955, "bottom"]
        self.rooms["113"] = [2.905, 5.710, 3.333, 6.237, "right"]
        self.rooms["114"] = [3.562, 5.24, 4.600, 6.736, "top"]
        self.rooms["115"] = [2.693, 6.237, 3.333, 7.459, "right"]
        self.rooms["116"] = [3.562, 6.736, 4.600, 7.988, "left"]
        self.rooms["118B"] = [4.41, 1.561, 5.62, 2.52, "right"]
        self.rooms["118A"] = [4.41, 2.52, 5.878, 4.198, "bottom"]
        self.rooms["118C"] = [5.878, 2.52, 6.931, 4.198, "left"]
        self.rooms["118D"] = [5.878, 1.561, 6.931, 2.52, "left"]
        self.rooms["male_1"] = [1.777, 4.198, 2.253, 4.955, "bottom"]
        self.rooms["female_1"] = [2.253, 4.198, 2.730, 4.955, "bottom"]
        self.rooms["117A"] = [5.300, 7.043, 6.509, 8.298, "left"]
        self.rooms["117B"] = [6.509, 7.043, 7.72, 8.298, "right"]
        self.rooms["117C"] = [5.300, 5.752, 6.931, 7.043, "bottom"]
        self.rooms["120"] = [6.931, 5.752, 7.72, 7.043, "right"]
        self.rooms["122"] = [6.931, 4.541, 7.72, 5.193, "right"]
        self.rooms["124A"] = [6.931, 2.866, 7.72, 3.987, "right"]
        self.rooms["124B"] = [6.931, 1.746, 7.72, 2.866, "right"]
        self.rooms["126"] = [6.931, 0.05, 7.72, .678, "right"]
        self.rooms["male_1_2"] = [6.931, 5.193, 7.72, 5.752, "right"]
        self.rooms["female_1_2"] = [6.931, .678, 7.72, 1.23, "right"]
        self.rooms["119"] = [8.094, 5.752, 9.533, 7.819, "left"]
        self.rooms["121"] = [8.094, 5.029, 8.864, 5.459, "left"]
        self.rooms["123A"] = [8.094, 4.406, 8.864, 5.029, "left"]
        self.rooms["123B"] = [8.094, 3.788, 8.864, 4.406, "left"]
        self.rooms["125"] = [8.094, 3.343, 8.864, 3.788, "left"]
        self.rooms["127"] = [8.094, 2.891, 8.864, 3.343, "left"]
        self.rooms["129"] = [8.094, 2.400, 8.864, 2.891, "left"]
        self.rooms["131"] = [8.094, 1.923, 8.864, 2.400, "left"]
        self.rooms["133"] = [8.094, 1.214, 8.864, 1.923, "left"]
        self.rooms["135"] = [8.094, .715, 8.864, 1.214, "left"]
        self.rooms["137"] = [8.094, .05, 8.864, .351, "left"]
        #first floor hallways
        hallways["1"] = [7.72, .05, 8.094, 8.298]
        hallways["2"] = [4.6, 4.198, 7.72, 4.541]
        hallways["3"] = [4.6, 4.541, 5.3, 7.326]
        hallways["4"] = [.905, 4.955, 4.6, 5.24]
        hallways["5"] = [1.408, 4.198, 1.777, 4.955]
        hallways["6"] = [3.333, 5.24, 3.562, 7.775]
        hallways["7"] = [1.103, 7.445, 3.562, 7.775]
        hallways["8"] = [1.843, 5.24, 2.101, 7.445]
        hallways["9"] = [8.094, .351, 8.864, .715]
        #first floor closets
        closets["1"] = [5.30, 4.541, 6.931, 7.043]
        closets["2"] = [3.052, 4.198, 3.936, 4.955]
        closets["3"] = [2.485, 5.24, 2.905, 6.237]
        closets["4"] = [2.485, 6.237, 2.905, 6.868]
        closets["5"] = [8.094, 5.459, 8.864, 5.752]

        stairs1["1"] = [.905, 5.24, .905, 3.987, .111, 3.987, .507, 5.24]
        stairs1["2"] = [3.562, 7.988, 4.600, 7.988, 4.600, 8.82, 3.562, 8.64]

        # stairs1["2"] =
        # stairs1["3"] =
        # stairs1["4"] =
        #second floor self.rooms
        self.rooms2["201"] = [.895, 4.302, 1.781, 4.917, "bottom"]
        self.rooms2["female_2"] = [1.781, 4.302, 2.273, 4.917, "bottom"]
        self.rooms2["male_2"] = [2.273, 4.302, 2.738, 4.917, "bottom"]
        self.rooms2["203"] = [.895, 5.24, 1.478, 5.668, "right"]
        self.rooms2["202A"] = [2.713, 5.24, 3.693, 6.586, "right"]
        self.rooms2["202B"] = [1.714, 5.24, 2.713, 5.719, "left"]
        self.rooms2["202C"] = [1.714, 5.719, 2.713, 6.586, "top"]
        self.rooms2["206"] = [1.714, 6.586, 2.713, 7.111, "left"]
        self.rooms2["216"] = [2.713, 6.586, 3.693, 7.111, "right"]
        self.rooms2["204"] = [.895, 5.668, 1.478, 6.132, "right"]
        self.rooms2["205"] = [.895, 6.132, 1.478, 6.586, "right"]
        self.rooms2["207"] = [.895, 6.586, 1.478, 7.382, "right"]
        self.rooms2["208"] = [.895, 7.382, 1.74, 8, "top"]
        self.rooms2["209"] = [1.74, 7.382, 2.27, 8, "top"]
        self.rooms2["210"] = [2.27, 7.382, 2.727, 8, "top"]
        self.rooms2["211"] = [2.727, 7.382, 3.173, 8, "top"]
        self.rooms2["212"] = [3.173, 7.382, 3.700, 8, "top"]
        self.rooms2["213"] = [3.968, 7.480, 4.576, 8, "left"]
        self.rooms2["214"] = [3.968, 7.027, 4.576, 7.480, "left"]
        self.rooms2["215"] = [3.968, 6.545, 4.576, 7.027, "left"]
        self.rooms2["217"] = [3.968, 6.107, 4.576, 6.545, "left"]
        self.rooms2["218"] = [3.968, 5.685, 4.576, 6.107, "left"]
        self.rooms2["219"] = [3.968, 5.24, 4.576, 5.685, "left"]
        self.rooms2["220"] = [3.968, 4.302, 4.576, 5.24, "bottom"]
        self.rooms2["221"] = [7.895, 4.541, 8.864, 5.193, "top"]
        self.rooms2["221A"] = [7.895, 5.193, 8.864, 5.752, "top"]
        self.rooms2["222"] = [6.931, 4.541, 7.895, 5.193, "top"]
        self.rooms2["222A"] = [6.931, 5.193, 7.895, 5.752, "top"]
        self.rooms2["223"] = [8.094, 3.343, 8.864, 4.541, "left"]
        self.rooms2["224"] = [6.931, 3.513, 7.72, 3.987, "right"]
        self.rooms2["225"] = [8.094, 2.891, 8.864, 3.343, "left"]
        self.rooms2["226"] = [6.931, 2.248, 7.72, 3.513, "right"]
        self.rooms2["227"] = [8.094, 2.400, 8.864, 2.891, "left"]
        self.rooms2["228"] = [6.931, 1.746, 7.72, 2.248, "right"]
        self.rooms2["229"] = [8.094, 1.923, 8.864, 2.400, "left"]
        self.rooms2["230"] = [6.931, 0.05, 7.895, 1.214, "bottom"]
        self.rooms2["231"] = [8.094, 1.214, 8.864, 1.604, "bottom"]
        self.rooms2["232"] = [7.895, 0.05, 8.864, 1.214, "bottom"]
        #second floor hallways
        hallways2["1"] = [.895, 4.917, 3.968, 5.24]
        hallways2["2"] = [1.478, 5.24, 1.714, 7.382]
        hallways2["3"] = [1.714, 7.111, 3.968, 7.382]
        hallways2["4"] = [3.693, 5.24, 3.968, 8]
        hallways2["5"] = [7.72, 1.214, 8.094, 4.541]
        hallways2["6"] = [8.094, 1.604, 8.864, 1.923]
        # hallways2["7"] = [1.103, 7.445, 3.562, 7.775]
        # hallways2["8"] = [1.843, 5.24, 2.101, 7.445]
        #second floor closets
        closets2["1"] = [3.052, 4.302, 3.968, 4.917]

        #third floor self.rooms
        self.rooms3["301"] = [.895, 4.302, 1.338, 4.917, "bottom"]
        self.rooms3["302"] = [1.338, 4.302, 1.781, 4.917, "bottom"]
        self.rooms3["female_3"] = [1.781, 4.302, 2.273, 4.917, "bottom"]
        self.rooms3["male_3"] = [2.273, 4.302, 2.738, 4.917, "bottom"]
        self.rooms3["303"] = [.895, 5.24, 1.478, 5.668, "right"]
        self.rooms3["304A"] = [2.713, 5.24, 3.693, 6.130, "right"]
        self.rooms3["304B"] = [2.713, 6.130, 3.693, 7.111, "right"]
        self.rooms3["304C"] = [1.714, 6.130, 2.713, 7.111, "left"]
        self.rooms3["304D"] = [1.714, 5.24, 2.713, 6.130, "left"]
        self.rooms3["305"] = [.895, 5.668, 1.478, 6.132, "right"]
        self.rooms3["306"] = [.895, 6.132, 1.478, 6.586, "right"]
        self.rooms3["307"] = [.895, 6.586, 1.478, 7.382, "right"]
        self.rooms3["308"] = [.895, 7.382, 1.74, 8, "top"]
        self.rooms3["309"] = [1.74, 7.382, 2.27, 8, "top"]
        self.rooms3["310"] = [2.27, 7.382, 2.727, 8, "top"]
        self.rooms3["311"] = [2.727, 7.382, 3.173, 8, "top"]
        self.rooms3["312"] = [3.173, 7.382, 3.700, 8, "top"]
        self.rooms3["313"] = [3.968, 7.480, 4.576, 8, "left"]
        self.rooms3["314"] = [3.968, 7.027, 4.576, 7.480, "left"]
        self.rooms3["315"] = [3.968, 6.545, 4.576, 7.027, "left"]
        self.rooms3["316"] = [3.968, 6.107, 4.576, 6.545, "left"]
        self.rooms3["317"] = [3.968, 5.685, 4.576, 6.107, "left"]
        self.rooms3["318"] = [3.968, 5.249, 4.576, 5.685, "left"]
        self.rooms3["319"] = [3.968, 4.302, 4.576, 5.249, "bottom"]
        #second floor hallways
        hallways3["1"] = [.895, 4.917, 3.968, 5.24]
        hallways3["2"] = [1.478, 5.24, 1.714, 7.382]
        hallways3["3"] = [1.714, 7.111, 3.968, 7.382]
        hallways3["4"] = [3.693, 5.24, 3.968, 8]
        #second floor closets
        closets3["1"] = [3.052, 4.302, 3.968, 4.917]

        #elevator for each Floor
        elevator["1"] = [2.738, 4.198, 3.052, 4.955]
        elevator["2"] = [2.738, 4.302, 3.052, 4.917]
        elevator["3"] = [2.738, 4.302, 3.052, 4.917]

        self.frame = tk.Frame(self.nb, width=WIDTH, height=HEIGHT)
        self.map = tk.Canvas(self.frame, width=WIDTH, height=HEIGHT)
        self.nb.add(self.frame, text="First Floor")
        #add the first floor hallways to canvas
        self.drawRects(self.map, hallways, "#b2bec3")
        #add the first floor closets
        self.drawRects(self.map, closets, "#000000")
        #add the first floor self.rooms to canvas
        self.drawRooms(self.map, self.rooms)

        #add the first floor elevator to canvas
        self.map.create_rectangle(elevator["1"][0]/10*WIDTH, elevator["1"][1]/10*HEIGHT, elevator["1"][2]/10*WIDTH, elevator["1"][3]/10*HEIGHT, \
                              fill="#00cec9", tags="ev1")
        self.drawStairs(self.map, stairs1, "#636e72") 
        self.map.bind("<Button-1>", self.clicked)

        self.second_floor = tk.Frame(self.nb, width=WIDTH, height=HEIGHT)
        self.map2 = tk.Canvas(self.second_floor, width=WIDTH, height=HEIGHT)
        ev2 = self.map2.create_rectangle(elevator["2"][0]/10*WIDTH, elevator["2"][1]/10*HEIGHT, elevator["2"][2]/10*WIDTH, elevator["2"][3]/10*HEIGHT, \
                              fill="#00cec9")
        #add the second floor hallways to canvas
        self.drawRects(self.map2, hallways2, "#b2bec3")
        #add the second floor closets
        self.drawRects(self.map2, closets2, "#000000")
        #add the second floor rooms
        self.drawRooms(self.map2, self.rooms2)
        self.drawStairs(self.map2, stairs1, "#636e72") 

        self.nb.add(self.second_floor, text="Second Floor")
        self.map2.bind("<Button-1>", self.clicked)

        self.third_floor = tk.Frame(self.nb, width=WIDTH, height=HEIGHT)
        self.map3 = tk.Canvas(self.third_floor, width=WIDTH, height=HEIGHT)
        ev3 = self.map3.create_rectangle(elevator["3"][0]/10*WIDTH, elevator["3"][1]/10*HEIGHT, elevator["3"][2]/10*WIDTH, elevator["3"][3]/10*HEIGHT, \
                              fill="#00cec9")
        #add the third floor hallways to canvas
        self.drawRects(self.map3, hallways3, "#b2bec3")
        #add the third floor closets
        self.drawRects(self.map3, closets3, "#000000")
        #add the third floor rooms
        self.drawRooms(self.map3, self.rooms3)
        self.drawStairs(self.map3, stairs1, "#636e72") 
        self.nb.add(self.third_floor, text="Third Floor")
        self.map3.bind("<Button-1>", self.clicked)

        self.map.pack()
        self.map2.pack()
        self.map3.pack()
        self.source = True

    def drawRooms(self, canvas, rooms):
        for i, room in rooms.items():
            x1 = room[0]/10*WIDTH
            x2 = room[2]/10*WIDTH
            y1= room[1]/10*HEIGHT
            y2= room[3]/10*HEIGHT
            canvas.create_rectangle(x1, y1, x2, y2, fill="#0984e3", activefill="#74b9ff", tags=i)
            canvas.create_text((x1+x2)/2, (y1+y2)/2, text=i)

    def drawRects(self, canvas, shapes, color):
        for i, room in shapes.items():
            x1 = room[0]/10*WIDTH
            x2 = room[2]/10*WIDTH
            y1= room[1]/10*HEIGHT
            y2= room[3]/10*HEIGHT
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="", tags=i)
    
    def drawStairs(self, canvas, stairs, color):
        for i, room in stairs.items():
            x1 = room[0]/10*WIDTH
            x2 = room[2]/10*WIDTH
            x3 = room[4]/10*WIDTH
            x4 = room[6]/10*WIDTH

            y1= room[1]/10*HEIGHT
            y2= room[3]/10*HEIGHT
            y3= room[5]/10*HEIGHT
            y4= room[7]/10*HEIGHT

            canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=color, outline="", tags=i)

    def selectSource(self):
        self.source = True

    def selectDest(self):
        self.source = False

    def clicked(self, event):
        if self.nb.index("current") == 0:
            canvas = self.map
        elif self.nb.index("current") == 1:
            canvas = self.map2
        elif self.nb.index("current") == 2:
            canvas = self.map3

        item = canvas.find_closest(event.x, event.y)
        item_type = canvas.type(item)
        if item_type == "rectangle":
            if self.source == True:
                clickedItem = canvas.itemcget(item, 'tag').split()[0]
                if clickedItem in list(self.rooms.keys()) + list(self.rooms2.keys()) + list(self.rooms3.keys()):
                    self.sourceVar.set(clickedItem)
            else:
                clickedItem = canvas.itemcget(item, 'tag').split()[0]
                if clickedItem in list(self.rooms.keys()) + list(self.rooms2.keys()) + list(self.rooms3.keys()):
                    self.destVar.set(clickedItem)

    def findShortest(self, source, dest):
        all_rooms = list(self.rooms.keys()) + list(self.rooms2.keys()) + list(self.rooms3.keys())
        if source in all_rooms and dest in all_rooms:
            self.map.delete('line')
            self.map2.delete('line')
            self.map3.delete('line')
            self.drawPath(self.controller.findShortest(source, dest).nodes)
        else:
            messagebox.showerror("Invalid Room", "Sorry! It appears the room you entered is not valid.")

    def drawPath(self, path):
        print(path)
        prev = [None, None]
        for step in path:
            #select the correct floor
            if step in self.rooms.keys():
                self.nb.select(0)
                room = self.rooms[step]
                canvas = self.map
            elif step in self.rooms2.keys():
                self.nb.select(1)
                room = self.rooms2[step]
                canvas = self.map2
            elif step in self.rooms3.keys():
                self.nb.select(2)
                room = self.rooms3[step]
                canvas = self.map3


            if room[4] == "left":
                current = [room[0]-.2, (room[1]+room[3])/2]
            elif room[4] == "right":
                current = [room[2]+.2, (room[1]+room[3])/2]
            elif room[4] == "top":
                current = [(room[0]+room[2])/2, room[1]-.2]
            elif room[4] == "bottom":
                current = [(room[0]+room[2])/2, room[3]+.2]
            if prev[0] == None:
                prev = current
                continue
            else:
                time.sleep(.25)
                canvas.create_line(prev[0]/10*WIDTH, prev[1]/10*HEIGHT, current[0]/10*WIDTH, current[1]/10*HEIGHT \
                                     , fill="#d63031", arrow=tk.LAST, width=2.5, tags="line")
                canvas.update()
                prev = current

if __name__ == "__main__":
    view = View(Controller())
    tk.mainloop()
