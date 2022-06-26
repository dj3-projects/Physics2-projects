import matplotlib.pyplot as plt 
import numpy as np
import math


# 물리값 기본 설정
g = 9.81 
dt = 0.1
t = 0 

angle = np.array([15, 30, 45, 60]) # 각도 설정
throw_v = 20
trajectories = [[(0,0)] for _ in range(len(angle))]
dones = np.zeros_like(angle, dtype=np.bool)
all_done = False

fig, ax = plt.subplots()

while(not all_done):
  ax.cla()
  ax.set_title("Throw the ball!")
  ax.set_xlim(-1, 600)
  ax.set_ylim(-1, 200)


  for i in range(len(angle)):
    x, y = zip(*trajectories[i])
    ax.scatter(x,y, label=angle[i])
  ax.legend()

  t = t + dt # 총 시간 = 처음 시간 + 변화한 시간

  for i in range(len(angle)):
    last_x, last_y = trajectories[i][-1]
    w = angle[i]

    next_x, next_y = last_x + throw_v*math.cos(w/180 *3.14), last_y + throw_v*math.sin(w/180 *3.14) - g * t # 포물선 운동 계산식

    if next_y <= 0: # y 0 도달시 종료 
      dones[i] = True
      continue

    trajectories[i].append((next_x, next_y))

  all_done = dones.all()

  plt.pause(0.01)

plt.show()
