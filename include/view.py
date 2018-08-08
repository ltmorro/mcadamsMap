#!/usr/bin/python3.5

import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import collections

DIM = 900
class Controller(object):
    def __init__(self):
        pass

    def findShortest(self, source, dest):
        print("Finding path from: " + source + " to " + dest)

class View(object):
    def __init__(self, controller):
        background_color = "#F5F5F5"
        button_font = "System 12"
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("McAdams Hall Map")
        self.root.bind("<Return>", lambda e: self.findShortest(self.sourceVar.get(), self.destVar.get()))
        self.sourceVar = tk.StringVar()
        self.destVar = tk.StringVar()
        self.selection = tk.Frame(self.root, width=DIM, height=DIM/4, bg=background_color)
        self.selection.pack(side=tk.BOTTOM)
        self.sourceBut = tk.Button(self.selection, text="Select Starting Point", command=self.selectSource, font=button_font)
        self.sourceBut.pack(side=tk.LEFT)
        self.source = tk.Entry(self.selection, text=self.sourceVar, font=button_font, width=10)
        self.source.pack(side=tk.LEFT)
        self.destBut = tk.Button(self.selection, text="Select Destination", command=self.selectDest, font=button_font)
        self.destBut.pack(side=tk.LEFT)
        self.dest = tk.Entry(self.selection, text=self.destVar, font=button_font, width=10)
        self.dest.pack(side=tk.LEFT)
        self.search = tk.Button(self.selection, text="Find Directions", command=lambda: self.findShortest(self.sourceVar.get(), self.destVar.get()), font=button_font)
        self.search.pack(side=tk.LEFT)
        self.reset = tk.Button(self.selection, text="Reset", command=self.reset, font=button_font)
        self.reset.pack(side=tk.LEFT)
        self.nb = ttk.Notebook(self.root)
        self.nb.pack()

        self.frame = tk.Frame(self.nb, width=DIM, height=DIM, bg=background_color)
        self.map = tk.Canvas(self.frame, width=DIM, height=DIM, bg=background_color)
        self.nb.add(self.frame, text="First Floor")
        self.map.bind("<Button-1>", self.clicked)

        self.second_floor = tk.Frame(self.nb, width=DIM, height=DIM, bg=background_color)
        self.map2 = tk.Canvas(self.second_floor, width=DIM, height=DIM, bg=background_color)

        self.nb.add(self.second_floor, text="Second Floor")
        self.map2.bind("<Button-1>", self.clicked)

        self.third_floor = tk.Frame(self.nb, width=DIM, height=DIM, bg=background_color)
        self.map3 = tk.Canvas(self.third_floor, width=DIM, height=DIM, bg=background_color)

        self.nb.add(self.third_floor, text="Third Floor")
        self.map3.bind("<Button-1>", self.clicked)

        self.map.pack()
        self.map2.pack()
        self.map3.pack()
        self.source = True

        #self.rooms follow format upper left coord, lower right coord
        #in inches [x1, y1, x2, y2]
        self.elevator = collections.defaultdict(list)
        self.rooms = collections.defaultdict(list)
        self.hallways = collections.defaultdict(list)
        self.hallways2 = collections.defaultdict(list)
        self.hallways3 = collections.defaultdict(list)
        self.rooms2 = collections.defaultdict(list)
        self.rooms3 = collections.defaultdict(list)
        self.closets = collections.defaultdict(list)
        self.closets2 = collections.defaultdict(list)
        self.closets3 = collections.defaultdict(list)
        self.stairs1 = collections.defaultdict(list)
        self.stairs2 = collections.defaultdict(list)
        self.stairs3 = collections.defaultdict(list)
        self.elevator["1"] = [2.738, 4.198, 3.052, 4.955]

        self.initFirstFloor()
        self.initSecondFloor()
        self.initThirdFloor()

    def drawLegend(self, canvas):
        canvas.create_rectangle(.15/10*DIM, .05/10*DIM, 1.75/10*DIM, 1.25/10*DIM, fill="#000000")
        canvas.create_rectangle(.2/10*DIM, .1/10*DIM, .4/10*DIM, .3/10*DIM, fill="#522D80") #rooms
        canvas.create_text(.5/10*DIM, .2/10*DIM, text="Rooms", fill="#ffffff", anchor=tk.W)
        canvas.create_rectangle(.2/10*DIM, .4/10*DIM, .4/10*DIM, .6/10*DIM, fill="#636e72") #stairs/elevators
        canvas.create_text(.5/10*DIM, .5/10*DIM, text="Stairs/Elevators", fill="#ffffff", anchor=tk.W)
        canvas.create_rectangle(.2/10*DIM, .7/10*DIM, .4/10*DIM, .9/10*DIM, fill="#b2bec3") #hallways
        canvas.create_text(.5/10*DIM, .8/10*DIM, text="Hallways", fill="#ffffff", anchor=tk.W)
        canvas.create_rectangle(.2/10*DIM, 1.0/10*DIM, .4/10*DIM, 1.2/10*DIM, fill="#2d3436") #inaccessible
        canvas.create_text(.5/10*DIM, 1.1/10*DIM, text="Inaccessible", fill="#ffffff", anchor=tk.W)

    def drawRooms(self, canvas, rooms):
        for i, room in rooms.items():
            x1 = room[0]/10*DIM
            x2 = room[2]/10*DIM
            y1= room[1]/10*DIM
            y2= room[3]/10*DIM
            canvas.create_rectangle(x1, y1, x2, y2, fill="#522D80", activefill="#9b59b6", tags=i)
            canvas.create_text((x1+x2)/2, (y1+y2)/2, text=i, width=(x2-x1)*.8, fill="#ffffff", tags=i)

    def drawRects(self, canvas, shapes, border, color):
        for i, room in shapes.items():
            x1 = room[0]/10*DIM
            x2 = room[2]/10*DIM
            y1= room[1]/10*DIM
            y2= room[3]/10*DIM
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=border, tags=i)

    def drawStairs(self, canvas, stairs, color):
        for i, room in stairs.items():
            x1 = room[0]/10*DIM
            x2 = room[2]/10*DIM
            x3 = room[4]/10*DIM
            x4 = room[6]/10*DIM

            y1= room[1]/10*DIM
            y2= room[3]/10*DIM
            y3= room[5]/10*DIM
            y4= room[7]/10*DIM
            canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=color, outline="#000000", tags=i)

    def drawMcAdams(self, canvas):
        coordinates = [.905, 5.24, .507, 5.24, .111, 3.987, .905, 3.987, .905, 4.198, 1.408, 4.198, 1.408, 1.561, \
                       6.931, 1.561, 6.931, 0.05, 8.864, .05, 8.864, 5.752, 9.533, 5.752, 9.533, 7.819, 8.094, 7.819, \
                       8.094, 8.298, 4.600, 8.298, 4.600, 8.82, 3.562, 8.64, 3.562, 8.298, 3.333, 8.298, 3.333, 7.988, .895, 7.988, .895, 5.24]
        pixel_coords = [x/10*DIM for x in coordinates]
        canvas.create_polygon(pixel_coords, outline="#000000", width=7.5)

    def drawElev(self, canvas, elevator, color):
        for i, room in elevator.items():
            x1 = room[0]/10*DIM
            x2 = room[2]/10*DIM

            y1= room[1]/10*DIM
            y2= room[3]/10*DIM
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#000000", tags=i)

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
        if item_type == "rectangle" or item_type == "text":
            if self.source == True:
                clickedItem = canvas.itemcget(item, 'tag').split()[0]
                if clickedItem in list(self.rooms.keys()) + list(self.rooms2.keys()) + list(self.rooms3.keys()):
                    self.sourceVar.set(clickedItem)
            else:
                clickedItem = canvas.itemcget(item, 'tag').split()[0]
                if clickedItem in list(self.rooms.keys()) + list(self.rooms2.keys()) + list(self.rooms3.keys()):
                    self.destVar.set(clickedItem)


    def clearLines(self):
        self.map.delete('line')
        self.map2.delete('line')
        self.map3.delete('line')

    def reset(self):
        self.sourceVar.set("")
        self.destVar.set("")
        self.clearLines()

    def findShortest(self, source, dest):
        all_rooms = list(self.rooms.keys()) + list(self.rooms2.keys()) + list(self.rooms3.keys())
        if source in all_rooms and dest in all_rooms:
            self.clearLines()
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
                current = [room[4], room[5]]
                canvas = self.map
            elif step in self.rooms2.keys():
                self.nb.select(1)
                room = self.rooms2[step]
                current = [room[4], room[5]]
                canvas = self.map2
            elif step in self.rooms3.keys():
                self.nb.select(2)
                room = self.rooms3[step]
                current = [room[4], room[5]]
                canvas = self.map3
            elif step in self.path.keys():
                room = self.path[step]
                canvas = self.map
                current = [room[0], room[1]]
            elif step in self.path2.keys():
                room = self.path2[step]
                canvas = self.map2
                current = [room[0], room[1]]
            elif step in self.path3.keys():
                room = self.path3[step]
                canvas = self.map3
                current = [room[0], room[1]]

            if prev[0] == None:
                prev = current
                continue
            else:
                self.delay(.2)
                canvas.create_line(prev[0]/10*DIM, prev[1]/10*DIM, current[0]/10*DIM, current[1]/10*DIM \
                                     , fill="#F66733", arrow=tk.LAST, width=2.5, tags="line")
                canvas.update()
                prev = current

    def delay(self, amount):
        initial = time.clock()
        while(time.clock() - initial < amount):
            pass

    def initFirstFloor(self):
        #rooms are in format [x1, y1, x2, y2, door_x, door_y]
        self.rooms = {
            "101":[2.101, 6.868, 2.693, 7.459, 1.972, 7.1],
            "102":[.895, 6.808, 1.843, 7.445, 1.972, 7.1],
            "103":[2.101, 6.402, 2.485, 6.868, 1.972, 6.736],
            "104":[.895, 6.179, 1.843, 6.808, 1.972, 6.736],
            "105":[2.101, 5.710, 2.485, 6.402, 1.972, 5.945],
            "106":[.895, 5.710, 1.843, 6.179, 1.972, 5.945],
            "107":[2.101, 5.24, 2.485, 5.710, 1.972, 5.475],
            "108":[.895, 5.24, 1.843, 5.710, 1.972, 5.475],
            "109":[.905, 4.198, 1.408, 4.955, 1.592, 4.75],
            "110B":[1.408, 1.561, 2.460, 2.666, 1.592, 2.75],
            "110C":[2.460, 1.561, 2.974, 2.666, 2.717, 2.75],
            "110D":[3.394, 1.561, 4.41, 2.92, 3.2, 2.75],
            "110E":[3.394, 2.92, 4.41, 4.198, 3.2, 3],
            "110A":[1.408, 2.666, 3.394, 4.198, 1.592, 4.198],
            "111":[2.905, 5.24, 3.333, 5.710, 3.447, 5.6],
            "112":[3.936, 4.198, 4.600, 4.955, 4.036, 5.098],
            "113":[2.905, 5.710, 3.333, 6.237, 3.447, 6.1],
            "114":[3.562, 5.24, 4.600, 6.736, 4.036, 5.098],
            "115":[2.693, 6.237, 3.333, 7.459, 3.447, 6.4],
            "116":[3.562, 6.736, 4.600, 7.988, 3.447, 7.6],
            "118B":[4.41, 1.561, 5.62, 2.52, 5.778, 2.045],
            "118A":[4.41, 2.52, 5.878, 4.198, 4.75, 4.369],
            "118C":[5.878, 2.52, 6.931, 4.198, 5.778, 2.6],
            "118D":[5.878, 1.561, 6.931, 2.52, 5.778, 2.045],
            "male_1":[1.777, 4.198, 2.253, 4.955, 1.972, 5.098],
            "female_1":[2.253, 4.198, 2.730, 4.955, 2.491, 5.098],
            "117A":[5.300, 7.043, 6.509, 8.298, 5.2, 7.23],
            "117B":[6.509, 7.043, 7.72, 8.298, 7.907, 7.23],
            "117C":[5.300, 5.752, 6.931, 7.043, 5.500, 7.23],
            "120":[6.931, 5.752, 7.72, 7.043, 7.325, 7.23],
            "122":[6.931, 4.541, 7.72, 5.193, 7.907, 4.721],
            "124A":[6.931, 2.866, 7.72, 3.987, 7.907, 3.426],
            "124B":[6.931, 1.746, 7.72, 2.866, 7.907, 2.316],
            "126":[6.931, 0.05, 7.72, .678, 7.907, .533],
            "male_1_2":[6.931, 5.193, 7.72, 5.752, 7.907, 5.4725],
            "female_1_2":[6.931, .678, 7.72, 1.23, 7.907, .96],
            "119":[8.094, 5.752, 9.533, 7.819, 7.907, 5.901],
            "121":[8.094, 5.029, 8.864, 5.459, 7.907, 5.259],
            "123A":[8.094, 4.406, 8.864, 5.029, 7.907, 4.717],
            "123B":[8.094, 3.788, 8.864, 4.406, 7.907, 4.096],
            "125":[8.094, 3.343, 8.864, 3.788, 7.907,  3.565],
            "127":[8.094, 2.891, 8.864, 3.343, 7.907, 3.117],
            "129":[8.094, 2.400, 8.864, 2.891, 7.907, 2.645],
            "131":[8.094, 1.923, 8.864, 2.400, 7.907, 2.165],
            "133":[8.094, 1.214, 8.864, 1.923, 7.907, 1.401],
            "135":[8.094, .715, 8.864, 1.214, 8.479 ,.533],
            "137":[8.094, .05, 8.864, .351, 8.479 ,.533],
        }

        self.path = {
            "hall1":[1.592, 5.098],
            "hall2":[1.972, 5.098],
            "hall3":[3.447, 5.098],
            "hall4":[1.972, 7.6],
            "hall5":[4.75, 5.098],
            "hall6":[4.75, 4.369],
            "hall7":[7.907, 4.369],
            "stairs1":[.805, 5.098],
            "stairs2":[3.447, 8.12],
            "stairs3":[7.325, 4.369],
            "stairs4":[7.325, 1.401],
        }

        self.hallways = {
            "1":[7.72, .05, 8.094, 8.298],
            "2":[4.6, 4.198, 7.72, 4.541],
            "3":[4.6, 4.541, 5.3, 8.298],
            "4":[.905, 4.955, 4.6, 5.24],
            "5":[1.408, 4.198, 1.777, 4.955],
            "6":[3.333, 5.24, 3.562, 8.298],
            "7":[.895, 7.445, 3.562, 7.988],
            "8":[1.843, 5.24, 2.101, 7.445],
            "9":[8.094, .351, 8.864, .715],
            "10":[6.931, 1.23, 7.72, 1.561]
        }

        self.closets = {
            "1":[5.30, 4.541, 6.931, 7.043],
            "2":[3.052, 4.198, 3.936, 4.955],
            "3":[2.485, 5.24, 2.905, 6.237],
            "4":[2.485, 6.237, 2.905, 6.868],
            "5":[8.094, 5.459, 8.864, 5.752]
        }

        self.stairs1 = {
            "1":[.905, 5.24, .905, 3.987, .111, 3.987, .507, 5.24],
            "2":[3.562, 7.988, 4.600, 7.988, 4.600, 8.82, 3.562, 8.64],
            "3":[6.931, 1.561, 7.72, 1.561, 7.72, 1.746, 6.931, 1.746],
            "4":[6.931, 3.987, 7.72, 3.987, 7.72, 4.198, 6.931, 4.198]
        }

        self.drawFirstFloor()

    def initSecondFloor(self):
        self.rooms2 = {
            "201":[.895, 4.198, 1.781, 4.955, 1.596, 5.097],
            "female_2":[1.781, 4.198, 2.273, 4.955, 2.027, 5.097],
            "male_2":[2.273, 4.198, 2.738, 4.955, 2.5055, 5.097],
            "203":[.895, 5.24, 1.478, 5.668, 1.596, 5.45],
            "202A":[2.713, 5.24, 3.693, 6.586, 3.834, 5.463],
            "202B":[1.714, 5.24, 2.713, 5.719, 1.596, 5.45],
            "202C":[1.714, 5.719, 2.713, 6.586, 2.027, 5.45],
            "206":[1.714, 6.586, 2.713, 7.111, 1.596, 6.984],
            "216":[2.713, 6.586, 3.693, 7.111, 3.834, 6.786],
            "204":[.895, 5.668, 1.478, 6.132, 1.596, 5.9],
            "205":[.895, 6.132, 1.478, 6.586, 1.596, 6.359],
            "207":[.895, 6.586, 1.478, 7.382, 1.596, 6.984],
            "208":[.895, 7.382, 1.74, 8, 1.596, 7.246],
            "209":[1.74, 7.382, 2.27, 8, 2.005, 7.246],
            "210":[2.27, 7.382, 2.727, 8, 2.498, 7.246],
            "211":[2.727, 7.382, 3.173, 8, 2.95, 7.246],
            "212":[3.173, 7.382, 3.700, 8, 3.436, 7.246],
            "213":[3.968, 7.480, 4.576, 8, 3.834, 7.74],
            "214":[3.968, 7.027, 4.576, 7.480, 3.834, 7.253],
            "215":[3.968, 6.545, 4.576, 7.027, 3.834, 6.786],
            "217":[3.968, 6.107, 4.576, 6.545, 3.834, 6.326],
            "218":[3.968, 5.685, 4.576, 6.107, 3.834, 5.896],
            "219":[3.968, 5.24, 4.576, 5.685, 3.834, 5.463],
            "220":[3.968, 4.198, 4.576, 5.24, 3.834, 5.097],
            "221":[7.895, 4.541, 8.864, 5.193, 7.995, 4.369],
            "221A":[7.895, 5.193, 8.864, 5.752, 7.995, 5.3],
            "222":[6.931, 4.541, 7.895, 5.193, 7.795, 4.369],
            "222A":[6.931, 5.193, 7.895, 5.752, 7.795, 5.3],
            "223":[8.094, 3.343, 8.864, 4.541, 7.907, 4.369],
            "224":[6.931, 3.513, 7.72, 3.987, 7.907, 3.613],
            "225":[8.094, 2.891, 8.864, 3.343, 7.907, 3.153],
            "226":[6.931, 2.248, 7.72, 3.513, 7.907, 2.848],
            "227":[8.094, 2.400, 8.864, 2.891, 7.907, 2.791],
            "228":[6.931, 1.746, 7.72, 2.248, 7.907, 2.232],
            "229":[8.094, 1.923, 8.864, 2.400, 7.907, 2.232],
            "230":[6.931, 0.05, 7.895, 1.214, 7.795, 1.411],
            "231":[8.094, 1.214, 8.864, 1.604, 7.907, 1.411],
            "232":[7.895, 0.05, 8.864, 1.214, 7.995, 1.411]
        }

        self.path2 = {
            "hall1_2":[7.907, 4.369],
            "hall2_2":[7.907, 1.411],
            "stairs1_2":[.805, 5.098],
            "stairs2_2":[3.834, 8.12],
            "stairs3_2":[7.325, 4.369],
            "stairs4_2":[7.325, 1.401]
        }

        self.hallways2 = {
            "1":[.895, 4.955, 3.968, 5.24],
            "2":[1.478, 5.24, 1.714, 7.382],
            "3":[1.714, 7.111, 3.968, 7.382],
            "4":[3.693, 5.24, 3.968, 8],
            "5":[7.72, 1.214, 8.094, 4.541],
            "6":[8.094, 1.604, 8.864, 1.923],
            "7":[6.931, 1.214, 7.72, 1.561],
            "8":[6.931, 4.198, 7.72, 5.193]
        }

        self.closets2 = {
            "1":[3.052, 4.198, 3.968, 4.955]
        }

        self.stairs2 = {
            "1":[.905, 5.24, .905, 3.987, .111, 3.987, .507, 5.24],
            "2":[3.562, 7.988, 4.600, 7.988, 4.600, 8.82, 3.562, 8.64],
            "3":[6.931, 1.561, 7.72, 1.561, 7.72, 1.746, 6.931, 1.746],
            "4":[6.931, 3.987, 7.72, 3.987, 7.72, 4.198, 6.931, 4.198]
        }

        self.drawSecondFloor()

    def initThirdFloor(self):
        self.rooms3 = {
            "301":[.895, 4.198, 1.338, 4.955, 1.115, 5.097],
            "302":[1.338, 4.198, 1.781, 4.955, 1.559, 5.097],
            "female_3":[1.781, 4.198, 2.273, 4.955, 2.027, 5.097],
            "male_3":[2.273, 4.198, 2.738, 4.955, 2.5055, 5.097],
            "303":[.895, 5.24, 1.478, 5.668, 1.596, 5.45],
            "304A":[2.713, 5.24, 3.693, 6.130, 3.834, 5.463],
            "304B":[2.713, 6.130, 3.693, 7.111, 3.834, 6.786],
            "304C":[1.714, 6.130, 2.713, 7.111, 1.596, 6.984],
            "304D":[1.714, 5.24, 2.713, 6.130, 1.596, 5.45],
            "305":[.895, 5.668, 1.478, 6.132, 1.596, 5.9],
            "306":[.895, 6.132, 1.478, 6.586, 1.596, 6.359],
            "307":[.895, 6.586, 1.478, 7.382, 1.596, 6.984],
            "308":[.895, 7.382, 1.74, 8, 1.596, 7.246],
            "309":[1.74, 7.382, 2.27, 8, 2.005, 7.246],
            "310":[2.27, 7.382, 2.727, 8, 2.498, 7.246],
            "311":[2.727, 7.382, 3.173, 8, 2.95, 7.246],
            "312":[3.173, 7.382, 3.700, 8, 3.436, 7.246],
            "313":[3.968, 7.480, 4.576, 8, 3.834, 7.74],
            "314":[3.968, 7.027, 4.576, 7.480, 3.834, 7.253],
            "315":[3.968, 6.545, 4.576, 7.027, 3.834, 6.786],
            "316":[3.968, 6.107, 4.576, 6.545, 3.834, 6.326],
            "317":[3.968, 5.685, 4.576, 6.107, 3.834, 5.896],
            "318":[3.968, 5.249, 4.576, 5.685, 3.834, 5.463],
            "319":[3.968, 4.198, 4.576, 5.249, 3.834, 5.097]
        }

        self.path3 = {
            "stairs1_3":[.805, 5.098],
            "stairs2_3":[3.834, 8.12]
        }

        self.hallways3 = {
            "1":[.895, 4.955, 3.968, 5.24],
            "2":[1.478, 5.24, 1.714, 7.382],
            "3":[1.714, 7.111, 3.968, 7.382],
            "4":[3.693, 5.24, 3.968, 8]
        }

        self.closets3 = {
            "1":[3.052, 4.198, 3.968, 4.955]
        }

        self.stairs3 = {
            "1":[.905, 5.24, .905, 3.987, .111, 3.987, .507, 5.24],
            "2": [3.562, 7.988, 4.600, 7.988, 4.600, 8.82, 3.562, 8.64]
        }

        self.drawThirdFloor()


    def drawFirstFloor(self):
        self.drawMcAdams(self.map)
        self.drawLegend(self.map)
        #add the first floor hallways to canvas
        self.drawRects(self.map, self.hallways, "", "#b2bec3")
        #add the first floor closets
        self.drawRects(self.map, self.closets, "#000000", "#2d3436")
        #add the first floor self.rooms to canvas
        self.drawRooms(self.map, self.rooms)

        #add the first floor elevator to canvas
        self.drawElev(self.map, self.elevator, "#636e72")
        self.drawStairs(self.map, self.stairs1, "#636e72")

    def drawSecondFloor(self):
        self.drawMcAdams(self.map2)
        self.drawLegend(self.map2)
        #add the second floor hallways to canvas
        self.drawRects(self.map2, self.hallways2, "", "#b2bec3")
        #add the second floor closets
        self.drawRects(self.map2, self.closets2, "#000000", "#2d3436")
        #add the second floor rooms
        self.drawRooms(self.map2, self.rooms2)
        self.drawStairs(self.map2, self.stairs2, "#636e72")
        self.drawElev(self.map2, self.elevator, "#636e72")

    def drawThirdFloor(self):
        #add the outline of mcadams to canvas
        self.drawMcAdams(self.map3)
        self.drawLegend(self.map3)
        #add the third floor hallways to canvas
        self.drawRects(self.map3, self.hallways3, "", "#b2bec3")
        #add the third floor closets
        self.drawRects(self.map3, self.closets3, "#000000", "#2d3436")
        #add the third floor rooms
        self.drawRooms(self.map3, self.rooms3)
        self.drawStairs(self.map3, self.stairs3, "#636e72")
        self.drawElev(self.map3, self.elevator, "#636e72")
if __name__ == "__main__":
    view = View(Controller())
    tk.mainloop()
