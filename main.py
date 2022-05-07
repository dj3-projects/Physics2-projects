from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = Tk()
root.title("포물선 운동 시뮬레이션")
root.geometry("1080x720")


graph_frame = Frame(root, relief="solid", bd=3, bg="white")
graph_frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

info_frame = Frame(root, width=230, bg="white")
info_frame.grid(row=0, column=2, columnspan=2, sticky="nsew")


root.mainloop()
