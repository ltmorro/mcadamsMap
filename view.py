#!/usr/bin/python3.5

import tkinter as tk
from tkinter import ttk
import collections
WIDTH = 1024
HEIGHT = 1024
root = tk.Tk()
nb = ttk.Notebook(root)
nb.pack()
#rooms follow format upper left coord, lower right coord
#in inches [x1, y1, x2, y2]
elevator = collections.defaultdict(list)
rooms = collections.defaultdict(list)
hallways = collections.defaultdict(list)
rooms2 = collections.defaultdict(list)
rooms3 = collections.defaultdict(list)
closets = collections.defaultdict(list)
closets2 = collections.defaultdict(list)
closets3 = collections.defaultdict(list)
rooms["101"] = [2.101, 6.868, 2.693, 7.459]
rooms["102"] = [1.103, 6.808, 1.843, 7.445]
rooms["103"] = [2.101, 6.402, 2.485, 6.868]
rooms["104"] = [1.103, 6.179, 1.843, 6.808]
rooms["105"] = [2.101, 5.710, 2.485, 6.402]
rooms["106"] = [1.103, 5.710, 1.843, 6.179]
rooms["107"] = [2.101, 5.24, 2.485, 5.710]
rooms["108"] = [1.103, 5.24, 1.843, 5.710]
rooms["109"] = [.905, 4.198, 1.408, 4.955]
rooms["110B"] = [1.408, 1.561, 2.460, 2.666]
rooms["110C"] = [2.460, 1.561, 2.974, 2.666]
rooms["110D"] = [3.394, 1.561, 4.41, 2.92]
rooms["110E"] = [3.394, 2.92, 4.41, 4.198]
rooms["110A"] = [1.408, 2.666, 3.394, 4.198]
rooms["111"] = [2.905, 5.24, 3.333, 5.710]
rooms["112"] = [3.936, 4.198, 4.600, 4.955]
rooms["113"] = [2.905, 5.710, 3.333, 6.237]
rooms["114"] = [3.562, 5.24, 4.600, 6.736]
rooms["115"] = [2.693, 6.237, 3.333, 7.455]
rooms["116"] = [3.562, 6.736, 4.600, 7.988]
rooms["118B"] = [4.41, 1.561, 5.62, 2.52]
rooms["118A"] = [4.41, 2.52, 5.878, 4.198]
rooms["118C"] = [5.878, 2.52, 6.931, 4.198]
rooms["118D"] = [5.878, 1.561, 6.931, 2.52]
rooms["male_1"] = [1.777, 4.198, 2.253, 4.955]
rooms["female_1"] = [2.253, 4.198, 2.730, 4.955]
rooms["117A"] = [5.300, 7.043, 6.509, 8.298]
rooms["117B"] = [6.509, 7.043, 7.72, 8.298]
rooms["117C"] = [5.300, 5.752, 6.931, 7.043]
rooms["120"] = [6.931, 5.752, 7.72, 7.043]
rooms["122"] = [6.931, 4.541, 7.72, 5.193]
rooms["124A"] = [6.931, 2.866, 7.72, 3.987]
rooms["124B"] = [6.931, 1.746, 7.72, 2.866]
rooms["126"] = [6.931, 0.05, 7.72, .678]
rooms["male_1_2"] = [6.931, 5.193, 7.72, 5.752]
rooms["female_1_2"] = [6.931, .678, 7.72, 1.23]
rooms["119"] = [8.094, 5.752, 9.533, 7.819]
rooms["121"] = [8.094, 5.029, 8.864, 5.459]
rooms["123A"] = [8.094, 4.406, 8.864, 5.029]
rooms["123B"] = [8.094, 3.788, 8.864, 4.406]
rooms["125"] = [8.094, 3.343, 8.864, 3.788]
rooms["127"] = [8.094, 2.891, 8.864, 3.343]
rooms["129"] = [8.094, 2.400, 8.864, 2.891]
rooms["131"] = [8.094, 1.923, 8.864, 2.400]
rooms["133"] = [8.094, 1.214, 8.864, 1.923]
rooms["135"] = [8.094, .715, 8.864, 1.214]
rooms["137"] = [8.094, .05, 8.864, .351]
#first floor hallways
hallways["1"] = [7.72, .05, 8.094, 8.298]
hallways["2"] = [4.6, 4.198, 7.72, 4.541]
hallways["3"] = [4.6, 4.541, 5.3, 7.326]
hallways["4"] = [.905, 4.955, 4.6, 5.24]
hallways["5"] = [1.408, 4.198, 1.777, 4.955]
hallways["6"] = [3.333, 5.24, 3.562, 7.775]
hallways["7"] = [1.103, 7.445, 3.562, 7.775]
hallways["8"] = [1.843, 5.24, 2.101, 7.445]
#second floor rooms
rooms2["201"] = [.895, 4.302, 1.781, 4.917]
rooms2["female_2"] = [1.781, 4.302, 2.273, 4.917]
rooms2["male_2"] = [2.273, 4.302, 2.738, 4.917]
rooms2["203"] = [.895, 5.183, 1.478, 5.668]
rooms2["202A"] = [2.713, 5.145, 3.693, 6.130]
rooms2["202B"] = [2.713, 6.130, 3.693, 7.111]
# rooms2["202C"] =
rooms2["206"] = [1.714, 6.130, 2.713, 7.111]
rooms2["216"] = [1.714, 5.145, 2.713, 6.130]
rooms2["204"] = [.895, 5.668, 1.478, 6.132]
rooms2["205"] = [.895, 6.132, 1.478, 6.586]
rooms2["207"] = [.895, 6.586, 1.478, 7.382]
rooms2["208"] = [.895, 7.382, 1.74, 8]
rooms2["209"] = [1.74, 7.382, 2.27, 8]
rooms2["210"] = [2.27, 7.382, 2.727, 8]
rooms2["211"] = [2.727, 7.382, 3.173, 8]
rooms2["212"] = [3.173, 7.382, 3.700, 8]
rooms2["213"] = [3.968, 7.480, 4.576, 8]
rooms2["214"] = [3.968, 7.027, 4.576, 7.480]
rooms2["215"] = [3.968, 6.545, 4.576, 7.027]
rooms2["217"] = [3.968, 6.107, 4.576, 6.545]
rooms2["218"] = [3.968, 5.685, 4.576, 6.107]
rooms2["219"] = [3.968, 5.249, 4.576, 5.685]
rooms2["220"] = [3.968, 4.302, 4.576, 5.249]
rooms2["221"] = [7.895, 4.541, 8.864, 5.193]
rooms2["221A"] = [7.895, 5.193, 8.864, 5.752]
rooms2["222"] = [6.931, 4.541, 7.895, 5.193]
rooms2["222A"] = [6.931, 5.193, 7.895, 5.752]
rooms2["223"] = [8.094, 3.343, 8.864, 4.541]
rooms2["224"] = [6.931, 3.513, 7.72, 3.987]
rooms2["225"] = [8.094, 2.891, 8.864, 3.343]
rooms2["226"] = [6.931, 2.248, 7.72, 3.513]
rooms2["227"] = [8.094, 2.400, 8.864, 2.891]
rooms2["228"] = [6.931, 1.746, 7.72, 2.248]
rooms2["229"] = [8.094, 1.923, 8.864, 2.400]
rooms2["230"] = [6.931, 0.05, 7.895, 1.214]
rooms2["231"] = [8.094, 1.214, 8.864, 1.604]
rooms2["232"] = [7.895, 0.05, 8.864, 1.214]
#third floor rooms
rooms3["301"] = [.895, 4.302, 1.338, 4.917]
rooms3["302"] = [1.338, 4.302, 1.781, 4.917]
rooms3["female_3"] = [1.781, 4.302, 2.273, 4.917]
rooms3["male_3"] = [2.273, 4.302, 2.738, 4.917]
rooms3["303"] = [.895, 5.183, 1.478, 5.668]
rooms3["304A"] = [2.713, 5.145, 3.693, 6.130]
rooms3["304B"] = [2.713, 6.130, 3.693, 7.111]
rooms3["304C"] = [1.714, 6.130, 2.713, 7.111]
rooms3["304D"] = [1.714, 5.145, 2.713, 6.130]
rooms3["305"] = [.895, 5.668, 1.478, 6.132]
rooms3["306"] = [.895, 6.132, 1.478, 6.586]
rooms3["307"] = [.895, 6.586, 1.478, 7.382]
rooms3["308"] = [.895, 7.382, 1.74, 8]
rooms3["309"] = [1.74, 7.382, 2.27, 8]
rooms3["310"] = [2.27, 7.382, 2.727, 8]
rooms3["311"] = [2.727, 7.382, 3.173, 8]
rooms3["312"] = [3.173, 7.382, 3.700, 8]
rooms3["313"] = [3.968, 7.480, 4.576, 8]
rooms3["314"] = [3.968, 7.027, 4.576, 7.480]
rooms3["315"] = [3.968, 6.545, 4.576, 7.027]
rooms3["316"] = [3.968, 6.107, 4.576, 6.545]
rooms3["317"] = [3.968, 5.685, 4.576, 6.107]
rooms3["318"] = [3.968, 5.249, 4.576, 5.685]
rooms3["319"] = [3.968, 4.302, 4.576, 5.249]
#elevator for each Floor
elevator["1"] = [2.738, 4.198, 3.052, 4.955]
elevator["2"] = [2.738, 4.302, 3.052, 4.917]
elevator["3"] = [2.738, 4.302, 3.052, 4.917]
frame = tk.Frame(nb, width=WIDTH, height=HEIGHT)

map = tk.Canvas(frame, width=WIDTH, height=HEIGHT)
map.create_rectangle(elevator["1"][0]/10*WIDTH, elevator["1"][1]/10*HEIGHT, elevator["1"][2]/10*WIDTH, elevator["1"][3]/10*HEIGHT, \
                      fill="#00cec9")
nb.add(frame, text="First Floor")
map.pack()
for i, room in rooms.items():
    x1 = room[0]/10*WIDTH
    x2 = room[2]/10*WIDTH
    y1= room[1]/10*HEIGHT
    y2= room[3]/10*HEIGHT
    map.create_rectangle(x1, y1, x2, y2, fill="#0984e3", activefill="#74b9ff")
    map.create_text((x1+x2)/2, (y1+y2)/2, text=i)

for i, hallway in hallways.items():
    x1 = hallway[0]/10*WIDTH
    x2 = hallway[2]/10*WIDTH
    y1= hallway[1]/10*HEIGHT
    y2= hallway[3]/10*HEIGHT
    map.create_rectangle(x1, y1, x2, y2, fill="#b2bec3", outline="")

second_floor = tk.Frame(nb, width=WIDTH, height=HEIGHT)

map2 = tk.Canvas(second_floor, width=WIDTH, height=HEIGHT)
map2.create_rectangle(elevator["2"][0]/10*WIDTH, elevator["2"][1]/10*HEIGHT, elevator["2"][2]/10*WIDTH, elevator["2"][3]/10*HEIGHT, \
                      fill="#00cec9")
for i, room in rooms2.items():
    x1 = room[0]/10*WIDTH
    x2 = room[2]/10*WIDTH
    y1= room[1]/10*HEIGHT
    y2= room[3]/10*HEIGHT
    map2.create_rectangle(x1, y1, x2, y2, fill="#0984e3", activefill="#74b9ff")
    map2.create_text((x1+x2)/2, (y1+y2)/2, text=i)
map2.pack()
nb.add(second_floor, text="Second Floor")

third_floor = tk.Frame(nb, width=WIDTH, height=HEIGHT)

map3 = tk.Canvas(third_floor, width=WIDTH, height=HEIGHT)
map3.create_rectangle(elevator["3"][0]/10*WIDTH, elevator["3"][1]/10*HEIGHT, elevator["3"][2]/10*WIDTH, elevator["3"][3]/10*HEIGHT, \
                      fill="#00cec9")
for i, room in rooms3.items():
    x1 = room[0]/10*WIDTH
    x2 = room[2]/10*WIDTH
    y1= room[1]/10*HEIGHT
    y2= room[3]/10*HEIGHT
    map3.create_rectangle(x1, y1, x2, y2, fill="#0984e3", activefill="#74b9ff")
    map3.create_text((x1+x2)/2, (y1+y2)/2, text=i)
map3.pack()
nb.add(third_floor, text="Third Floor")


root.mainloop()
# def createRoom(map, room):
#     #create top line
#     map.create_line(room[0], room[1], room[2], room[1])
#     #create left line
#     map.create_line(room[0], room[1], room[0], room[3])
#     #create bottom line
#     map.create_line(room[0], room[3], room[2], room[3])
