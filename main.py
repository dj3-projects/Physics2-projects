from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = Tk()
root.title("포물선 운동 시뮬레이션")
root.geometry("1080x720")


# 그래프가 출력될 프레임
graph_frame = Frame(root, relief="solid", bd=3, bg="white")
graph_frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

# 시뮬로 알 수 있는 정보들이 출력될 프레임
info_frame = Frame(root, width=230, bg="white")
info_frame.grid(row=0, column=2, columnspan=2, sticky="nsew")

# 사용자가 조절할 수 있는 값들의 입력공간이 보일 프레임
input_frame = Frame(root, width=230, relief="solid", bd=2, bg="white")
input_frame.grid(row=1, column=2, columnspan=2, sticky="nsew")


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()
