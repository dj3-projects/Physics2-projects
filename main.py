from tkinter import *
from tkinter.ttk import *

from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = Tk()
root.title("포물선 운동 시뮬레이션")
root.geometry("1080x720")
root.state("zoomed")


root.mainloop()
